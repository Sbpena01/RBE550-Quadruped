import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose
from custom_interface.msg import ImuData, LegState

import numpy as np
import threading
import time

class Leg(Node):
    def __init__(self, node_name: str, is_left = True):
        super().__init__(node_name)
        self.name = node_name
        self.joint_publisher = self.create_publisher(Float64MultiArray, '/'+node_name+'_controller/commands', 10)
        self.pose_subscriber = None
        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.updateOffsets, 1)

        self.l1=25
        self.l2=20
        self.l3=80
        self.l4=80
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
        if self.current_pose is None:
            self.current_pose = state.pose
            self.move()
            return
        self.is_swing = state.is_swing
        # self.get_logger().info(f"{self.is_swing}, {state.is_swing}")
        traj = self.generateTrajectory(state.pose)
        for col in traj.T:
            traj_pose = Pose()
            traj_pose.position.x = col[0]
            traj_pose.position.y = col[1]
            traj_pose.position.z = col[2]
            self.current_pose = traj_pose
            self.move()
            time.sleep(0.05)

    def move(self):
        # if not self.is_swing:
        #     self.current_pose.position.x += self.x_offset
        #     self.current_pose.position.z += self.z_offset
        self.shoulder, self.leg, self.foot = self.IK(self.current_pose)
        self.publish()

    def publish(self):
        data = [
            self.shoulder,
            self.leg,
            self.foot
        ]
        self.joint_publisher.publish(Float64MultiArray(data=data))

    def IK(self, pose: Pose):
        position = pose.position  # Point msg with X, Y, and Z float64s
        x = position.x
        y = position.y
        z = position.z
        
        # Calculations below are from SpotMicroAI, not calculated by us.
        # See: https://spotmicroai.readthedocs.io/en/latest/kinematic/

        F=np.sqrt(x**2+y**2-self.l1**2)
        G=F-self.l2  
        H=np.sqrt(G**2+z**2)
        
        if self.is_left:
            shoulder_angle=np.arctan2(y,x)+np.arctan2(F,-self.l1)
        else:
            shoulder_angle=-np.arctan2(y,x)-np.arctan2(F,-self.l1)

        D=(H**2-self.l3**2-self.l4**2)/(2*self.l3*self.l4)
        foot_angle=np.arccos(D) 

        leg_angle=np.arctan2(z,G)-np.arctan2(self.l4*np.sin(foot_angle),self.l3+self.l4*np.cos(foot_angle))
        
        return (shoulder_angle, leg_angle, foot_angle)

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
    
    def generateTrajectory(self, pose: Pose, height: float = 50):
        start = np.array([self.current_pose.position.x, self.current_pose.position.y, self.current_pose.position.z])
        end = np.array([pose.position.x, pose.position.y, pose.position.z])
        idx = 0
        time = 4
        length = int(10 * time)
        if self.is_swing:
            P1 = np.array([start[0], start[1]+height, start[2]])
            P2 = np.array([end[0], end[1]+height, end[2]])
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
    
