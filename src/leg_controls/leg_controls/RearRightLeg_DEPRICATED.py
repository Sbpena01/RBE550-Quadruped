#/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose

import time
import numpy as np

# CONSTANTS
INIT_X = -30.0
INIT_Y = -120.0
INIT_Z = 0.0

# Leg Lengths
l1=25
l2=20
l3=80
l4=80

class RearRightLeg(Node):
    def __init__(self):
        super().__init__('front_left_leg')
        self.joint_publisher = self.create_publisher(Float64MultiArray, '/rear_right_leg_controller/commands', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/rear_right_ee_pose', self.legIK, 10)
        initial_pose = Pose()
        initial_pose.position.x = INIT_X
        initial_pose.position.y = INIT_Y
        initial_pose.position.z = INIT_Z
        self.legIK(initial_pose)
        self.timer = self.create_timer(0.1, self.publish)
    
    def publish(self) -> None:
        angles = [
            self.shoulder_angle,
            self.leg_angle,
            self.foot_angle
        ]
        angle_array = Float64MultiArray(data=angles)
        self.joint_publisher.publish(angle_array)
    
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

        self.shoulder_angle=-np.arctan2(y,x)-np.arctan2(F,-l1)

        D=(H**2-l3**2-l4**2)/(2*l3*l4)
        self.foot_angle=np.arccos(D) 

        self.leg_angle=np.arctan2(z,G)-np.arctan2(l4*np.sin(self.foot_angle),l3+l4*np.cos(self.foot_angle))
        
        # print(self.shoulder_angle, self.leg_angle, self.foot_angle)
        # Publish the leg angles to Gazebo and PID controller
        self.publish()

def main(args=None):
    rclpy.init(args=args)
    rear_right_leg = RearRightLeg()
    rclpy.spin(rear_right_leg)


if __name__ == '__main__':
    main()
