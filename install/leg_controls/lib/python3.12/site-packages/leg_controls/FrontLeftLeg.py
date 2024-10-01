import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64
from geometry_msgs.msg import Pose
from sensor_msgs.msg import JointState

import time
import numpy as np

# CONSTANTS
FRONT_LEFT_SHOULDER_INIT = 0.0
FRONT_LEFT_LEG_INIT = 0.0
FRONT_LEFT_FOOT_INIT = 0.0

# Leg Lengths
l1=25
l2=20
l3=80
l4=80

class FrontLeftLeg(Node):
    def __init__(self):
        super().__init__('front_left_leg')
        self.shoulder_publisher_ = self.create_publisher(Float64, 'front_left_shoulder_position', 10)
        self.leg_publisher_ = self.create_publisher(Float64, 'front_left_leg_position', 10)
        self.foot_publisher_ = self.create_publisher(Float64, 'front_left_foot_position', 10)
        self.joint_state_publisher = self.create_publisher(JointState, 'joint_state', 10)
        self.shoulder_angle = FRONT_LEFT_SHOULDER_INIT
        self.leg_angle = FRONT_LEFT_LEG_INIT
        self.foot_angle = FRONT_LEFT_FOOT_INIT
    
    def publish(self) -> None:
        shoulder_angle_msg = Float64()
        shoulder_angle_msg.data = self.shoulder_angle
        leg_angle_msg = Float64()
        leg_angle_msg.data = self.leg_angle
        foot_angle_msg = Float64()
        foot_angle_msg.data = self.foot_angle
        self.shoulder_publisher_.publish(shoulder_angle_msg)
        self.leg_publisher_.publish(leg_angle_msg)
        self.foot_publisher_.publish(foot_angle_msg)
        
        # joint_state = JointState()
        # timestamp = self.get_clock().now()
        # joint_state.header.stamp = timestamp.to_msg()
        # joint_state.name = ['front_left_shoulder', 'front_left_leg', 'front_left_foot']
        # joint_state.position = [self.shoulder_angle, self.leg_angle, self.foot_angle]
    
    def legIK(self, msg: Pose):
        position = msg.position  # Point msg with X, Y, and Z float64s
        x = position.x
        y = position.y
        z = position.z
        orientation = msg.orientation  # Quaternion msg w/ X, Y, Z, and omega float64s
        
        # Calculations below are from SpotMicroAI, not calculated by us.
        # See: https://spotmicroai.readthedocs.io/en/latest/kinematic/

        F=np.sqrt(x**2+y**2-l1**2)
        G=F-l2  
        H=np.sqrt(G**2+z**2)

        self.shoulder_angle=-np.atan2(y,x)-np.atan2(F,-l1)

        D=(H**2-l3**2-l4**2)/(2*l3*l4)
        self.foot_angle=np.acos(D) 

        self.leg_angle=np.atan2(z,G)-np.atan2(l4*np.sin(self.foot_angle),l3+l4*np.cos(self.foot_angle))
        
        print(self.shoulder_angle, self.leg_angle, self.foot_angle)
        # Publish the leg angles to Gazebo and PID controller
        # self.publish()
        
        
        
def main(args=None):
    rclpy.init(args=args)
    front_left_leg = FrontLeftLeg()
    pose = Pose()
    pose.position.x = -55
    pose.position.y = -100
    pose.position.z = 20
    front_left_leg.legIK(pose)
    # while True:
    #     front_left_leg.publish()
    #     print('Publishing: ', front_left_leg.shoulder_angle, front_left_leg.leg_angle, front_left_leg.foot_angle)
    #     time.sleep(0.05)  # 20 Hz


if __name__ == '__main__':
    main()
