#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState

class RearRightLeg(Leg):
    def __init__(self):
        super().__init__('rear_right_leg', is_left=False)
        self.pose_subscriber = self.create_subscription(LegState, '/rear_right_ee_pose', self.moveThroughTrajectory, 10)
        self.rate = self.create_rate(10)  # 10 Hz

def main(args=None):
    rclpy.init(args=args)
    leg = RearRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
