import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose

import numpy as np

class Leg(Node):
    def __init__(self, node_name: str, is_left = True):
        super().__init__(node_name)
        self.joint_publisher = self.create_publisher(Float64MultiArray, node_name+'_controller/commands', 10)
        self.pose_subscriber = None

        self.l1=25
        self.l2=20
        self.l3=80
        self.l4=80
        self.shoulder = 0.0
        self.leg = 0.0
        self.foot = 0.0

        self.is_left = is_left  # Used in inverse kinematics
        self.is_swing = False  # Is the leg swinging or in its stance state (touching the ground)
        self.current_pose = None
        self.timer = self.create_timer(0.1, self.publish)
    
    def publish(self):
        data = [
            self.shoulder,
            self.leg,
            self.foot
        ]
        self.joint_publisher.publish(Float64MultiArray(data=data))
    
    def moveTo(self, pose: Pose):
        self.shoulder, self.leg, self.foot = self.IK(pose)
        self.publish()

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
    
