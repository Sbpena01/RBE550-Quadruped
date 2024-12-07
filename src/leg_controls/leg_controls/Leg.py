import rclpy
from rclpy.node import Node
# from rclpy import time
import time

from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose
from custom_interface.msg import ImuData, LegState

import numpy as np
import threading
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

from geometry_msgs.msg import TransformStamped, PoseStamped, Point

class Leg(Node):
    def __init__(self, node_name: str, is_left = True):
        super().__init__(node_name)
        self.name = node_name
        self.joint_publisher = self.create_publisher(Float64MultiArray, '/'+node_name+'_leg_controller/commands', 10)
        self.pose_subscriber = None
        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.updateOffsets, 1)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.25, self.publish)

        self.l0 = 0.0  # Base to shoulder
        self.l1 = 0.052  # shoulder to leg
        self.l2 = -0.12  # leg to foot
        self.l3 = -0.115 # foot to toe

        self.shoulder = 0.0
        self.leg = 0.0
        self.foot = 0.0

        # Data used for stability control
        self.waiting_event = threading.Event()
        self.imu_data = None
        self.x_offset = 0.0
        self.z_offset = 0.0

        self.is_left = is_left  # Used in inverse kinematics
        self.is_swing = False  # Is the leg swinging or in its stance state (touching the ground)
        self.current_pose = None

    def moveThroughTrajectory(self, state:LegState):
        if not state.is_swing:
            self.current_pose = state.pose
            self.move()
            return
        elif state.is_swing:
            self.is_swing = state.is_swing
            traj = self.generateTrajectory(state.pose)
            for col in traj.T:
                traj_pose = Pose()
                traj_pose.position.x = col[0]
                traj_pose.position.y = col[1]
                traj_pose.position.z = col[2]
                self.current_pose = traj_pose
                self.get_logger().info(f"{self.current_pose.position.x, self.current_pose.position.y, self.current_pose.position.z}")
                self.move()
                time.sleep(0.01)

    def move(self):
        self.shoulder, self.leg, self.foot = self.IK(self.current_pose)
        self.publish()

    def publish(self):
        data = [
            self.shoulder,
            self.leg,
            self.foot
        ]
        self.joint_publisher.publish(Float64MultiArray(data=data))

    def transformFromBaseLink(self, x, y, z):
        # These are values taken directly from URDF
        shiftx = 0.093
        shifty = 0.036
        match self.name:
            case 'front_left':
                x += -shiftx
                y += shifty
            case 'front_right':
                x += -shiftx
                y += -shifty
            case 'rear_left':
                x += shiftx
                y += shifty
            case 'rear_right':
                x += shiftx
                y += -shifty
        return x, y, z

    def IK(self, pose: Pose):
        x = pose.position.x
        y = pose.position.y
        z = pose.position.z
        x, y, z = self.transformFromBaseLink(x, y, z)

        # Shoulder Angle Calculation
        C = np.sqrt(z**2 + y**2)
        D = np.sqrt(C**2 - self.l1**2)
        alpha = np.arctan2(np.abs(y),np.abs(z))
        beta = np.arctan2(D, self.l1)
        shoulder = (alpha + beta) - (np.pi/2)

        # Leg Angle Calculation
        G = np.sqrt(D**2 + x**2)
        leg_prime = np.arccos((G**2 - self.l2**2 - self.l3**2)/(-2*self.l2*self.l3))
        foot = np.pi - leg_prime

        # Foot Angle Calculation
        alpha = np.arctan2(x, D)
        beta = np.arcsin((self.l3*np.sin(leg_prime))/G)
        leg = alpha + beta
        # if self.is_left:
        #     return (-shoulder, leg, foot)
        # else:
        return (shoulder, leg, foot)

    def updateOffsets(self, imu_data: ImuData):
        k_x = 2.0
        k_z = 2.0

        # The axes for the left and right legs are not the same and the offsets
        # must be consistent with each leg's frame
        if self.is_left:
            self.x_offset -= k_x * imu_data.roll
            self.z_offset -= k_z * imu_data.pitch
        else:
            self.x_offset += k_x * imu_data.roll
            self.z_offset -= k_z * imu_data.pitch
    
    def generateTrajectory(self, pose: Pose, height: float = 0.02):
        start = np.array([self.current_pose.position.x, self.current_pose.position.y, self.current_pose.position.z])
        end = np.array([pose.position.x, pose.position.y, pose.position.z])
        idx = 0
        time = 4
        length = int(10 * time)
        if self.is_swing:
            P1 = np.array([start[0], start[1], start[2]+height])
            P2 = np.array([end[0], end[1], end[2]+height])
            steps = np.linspace(0, 1, length)
            B = np.zeros((3, length))
            for step in steps:
                B[:, idx] = (1-step)**3*start + 3*(1-step)**2*step*P1 + 3*(1-step)*step**2*P2 + step**3*end
                idx += 1
        else:
            steps = np.linspace(0, 1, length)
            B = np.zeros((3, length))
            for step in steps:
                B[:, idx] = (1-step)*start + step*end
                idx += 1
        return B
    
    def getTransform(self, target:str, source:str) -> TransformStamped:
        try:
            transform = self.tf_buffer.lookup_transform(
                target,
                source,
                time.Time())
            # print("Found transform!")
            return transform
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {target} to {source}: {ex}')
            return TransformStamped()
