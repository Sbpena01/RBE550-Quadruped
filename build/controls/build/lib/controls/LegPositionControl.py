import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

# CONSTANTS
FRONT_LEFT_SHOULDER_INIT = 0.0
FRONT_LEFT_LEG_INIT = 0.0
FRONT_LEFT_FOOT_INIT = 0.0

class FrontLeftLeg(Node):
    def __init__(self):
        super().__init__('front_left_leg')
        self.shoulder_publisher_ = self.create_publisher(Float64, 'front_left_shoulder_position', 10)
        self.leg_publisher_ = self.create_publisher(Float64, 'front_left_leg_position', 10)
        self.foot_publisher_ = self.create_publisher(Float64, 'front_left_foot_position', 10)
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

def main():
    front_left_leg = FrontLeftLeg()
    while True:
        front_left_leg.publish()
        print('Publishing: ', front_left_leg.shoulder_angle, front_left_leg.leg_angle, front_left_leg.foot_angle)


if __name__ == '__main__':
    main()
