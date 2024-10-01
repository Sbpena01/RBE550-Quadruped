import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

import time

# CONSTANTS
REAR_RIGHT_SHOULDER_INIT = 0.0
REAR_RIGHT_LEG_INIT = 0.0
REAR_RIGHT_FOOT_INIT = 0.0

class RearRightLeg(Node):
    def __init__(self):
        super().__init__('rear_right_leg')
        self.shoulder_publisher_ = self.create_publisher(Float64, 'rear_right_shoulder_position', 10)
        self.leg_publisher_ = self.create_publisher(Float64, 'rear_right_leg_position', 10)
        self.foot_publisher_ = self.create_publisher(Float64, 'rear_right_foot_position', 10)
        self.shoulder_angle = REAR_RIGHT_SHOULDER_INIT
        self.leg_angle = REAR_RIGHT_LEG_INIT
        self.foot_angle = REAR_RIGHT_FOOT_INIT
    
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

def main(args=None):
    rclpy.init(args=args)
    rear_right_leg = RearRightLeg()
    while True:
        rear_right_leg.publish()
        print('Publishing: ', rear_right_leg.shoulder_angle, rear_right_leg.leg_angle, rear_right_leg.foot_angle)
        time.sleep(0.05)  # 20 Hz


if __name__ == '__main__':
    main()
