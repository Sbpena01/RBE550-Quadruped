import rclpy
from rclpy.node import Node
from rclpy import time

import rclpy.time
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import TransformStamped, Pose, PoseStamped
from custom_interface.msg import LegState
from nav_msgs.msg import Path

import numpy as np
import time as t

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener


class Leg(Node):
    def __init__(self, node_name: str, is_left = True):
        super().__init__(node_name)
        self.name = node_name
        self.joint_publisher = self.create_publisher(Float64MultiArray, '/'+node_name+'_leg_controller/commands', 10)
        self.swing_publisher = self.create_publisher(LegState, '/'+node_name+'_leg_state', 10)
        self.path_publisher = self.create_publisher(Path, '/swing_trajectory', 10)
        self.pose_subscriber = None
        
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

        self.is_left = is_left  # Used in inverse kinematics
        self.is_swing = False  # Is the leg swinging or in its stance state (touching the ground)
        self.turn_left = False
        self.turn_right = False
        self.current_pose = None
        self.home_pose = None
        self.initCurrentPose()

    def initCurrentPose(self):
        transform = self.getTransform(self.name+"_toe_link")
        while transform.transform.translation.x != 0.0:
            transform = self.getTransform(self.name+"_toe_link")
        self.get_logger().info(f"{self.name} Position Initialized")
        leg_pose = Pose()
        leg_pose.position.x = transform.transform.translation.x
        leg_pose.position.y = transform.transform.translation.y
        leg_pose.position.z = transform.transform.translation.z
        self.current_pose = Pose()

    def moveThroughTrajectory(self, state:LegState, visualize=True):
        self.is_swing = state.is_swing
        self.turn_left = state.turn_left
        self.turn_right = state.turn_right
        go_to_pose = state.pose
        if state.pose.position.x == 0.0:
            go_to_pose = self.home_pose
        traj = self.generateTrajectory(go_to_pose)
        if traj is None:
            self.is_swing = False  # Trajectory is over
            return
        path: list[PoseStamped] = []
        for col in traj.T:
            traj_pose = PoseStamped()
            traj_pose.header.frame_id = 'base_link'
            traj_pose.header.stamp = time.Time().to_msg()
            traj_pose.pose.position.x = col[0]
            traj_pose.pose.position.y = col[1]
            traj_pose.pose.position.z = col[2]
            path.append(traj_pose)
        if visualize:
            rviz_path = Path()
            rviz_path.header.frame_id = 'base_link'
            rviz_path.header.stamp = rclpy.time.Time().to_msg()
            rviz_path.poses = path
            self.path_publisher.publish(rviz_path)
        for node in path:
            self.current_pose = node.pose
            self.move()
            if self.name == 'rear_left':
                self.get_logger().info(f"{node.pose.position}")
            t.sleep(0.01)
        self.is_swing = False  # Trajectory is over
        self.turn_left = False
        self.turn_right = False

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
        state_data = LegState()
        state_data.is_swing = self.is_swing
        state_data.name = self.name
        transform = self.getTransform(self.name+"_toe_link")
        leg_pose = Pose()
        leg_pose.position.x = transform.transform.translation.x
        leg_pose.position.y = transform.transform.translation.y
        leg_pose.position.z = transform.transform.translation.z
        state_data.pose = leg_pose
        self.swing_publisher.publish(state_data)

    def transformFromBaseLink(self, x, y, z):
        # These are values taken directly from URDF
        shiftx = 0.093
        shifty = 0.036
        match self.name:
            case 'front_left':
                x += shiftx
                y += shifty
            case 'front_right':
                x += shiftx
                y += -shifty
            case 'rear_left':
                x += -shiftx
                y += shifty
            case 'rear_right':
                x += -shiftx
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
        alpha = np.arctan2(-x, D)
        beta = np.arcsin((self.l3*np.sin(leg_prime))/G)
        leg = alpha + beta
        return (shoulder, leg, foot)

    def generateTrajectory(self, pose: Pose, height: float = 0.02, turn_radius=0.02):
        start = np.array([self.current_pose.position.x, self.current_pose.position.y, self.current_pose.position.z])
        end = np.array([pose.position.x, pose.position.y, pose.position.z])
        if np.array_equal(start, end):
            return
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
        elif self.turn_left:
            match self.name:
                case 'front_left':
                    P1 = np.array([end[0], start[1], start[2]])
                case 'front_right':
                    P1 = np.array([start[0], end[1], start[2]])
                case 'rear_left':
                    P1 = np.array([start[0], end[1], start[2]])
                case 'rear_right':
                    P1 = np.array([end[0], start[1], start[2]])
            steps = np.linspace(0, 1, length)
            B = np.zeros((3, length))
            for step in steps:
                B[:, idx] = (1-step)**2*start + 2*(1-step)*step*P1 + step**2*end
                idx += 1
        else:
            steps = np.linspace(0, 1, length)
            B = np.zeros((3, length))
            for step in steps:
                B[:, idx] = (1-step)*start + step*end
                idx += 1
        return B
    
    def getTransform(self, source: str) -> TransformStamped:
        target = 'base_link'
        try:
            transform = self.tf_buffer.lookup_transform(
                target,
                source,
                time.Time())
            return transform
        except TransformException as ex:
            return TransformStamped()
