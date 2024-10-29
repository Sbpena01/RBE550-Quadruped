#/usr/bin/env python3
import rclpy
import rclpy.logging
import threading

from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose

import numpy as np
from GaitGenerator import WalkingGait


### CONSTANTS
# Starting joint angles (rad) for when the leg is initialized
INIT_X = -30.0
INIT_Y = -120.0
INIT_Z = 0.0

# Leg Lengths
l1=25
l2=20
l3=80
l4=80

class FrontLeftLeg(Node):
    def __init__(self):
        super().__init__('front_left_leg')
        self.joint_publisher = self.create_publisher(Float64MultiArray, '/front_left_leg_controller/commands', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/front_left_ee_pose', self.legIK, 10)

        self.shoulder_angle = 0.0
        self.leg_angle = 0.0
        self.foot_angle = 0.0
        initial_pose = Pose()
        initial_pose.position.x = INIT_X
        initial_pose.position.y = INIT_Y
        initial_pose.position.z = INIT_Z
        self.legIK(initial_pose)

        self.timer = self.create_timer(0.05, self.publish)
        
    
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

        try:
            F=np.sqrt(x**2+y**2-l1**2)
            G=F-l2  
            H=np.sqrt(G**2+z**2)

            self.shoulder_angle=np.arctan2(y,x)+np.arctan2(F,-l1)

            D=(H**2-l3**2-l4**2)/(2*l3*l4)
            if D < -1 or D > 1:
                print(f"Invalid value for arccos: {D}. Returning early.")
                return  # Early return if D is out of bounds
            
            self.foot_angle=np.arccos(D) 
            self.leg_angle=np.arctan2(z,G)-np.arctan2(l4*np.sin(self.foot_angle),l3+l4*np.cos(self.foot_angle))
        except Exception as e:
            print("Out of Bounds: ", e)
            return

        
        
def main(args=None):
    print("hey")
    rclpy.init(args=args)
    front_left_leg = FrontLeftLeg() 
    rclpy.spin(front_left_leg)



if __name__ == '__main__':
    main()
    rclpy.init(args=None)

    front_left_leg = FrontLeftLeg() 
    test_msg = Pose
    test_msg.position.x = 1
