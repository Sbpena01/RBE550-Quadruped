#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState

class FrontRightLeg(Leg):
    def __init__(self):
        super().__init__('front_right_leg', is_left=False)
        self.pose_subscriber = self.create_subscription(LegState, '/front_right_ee_pose', self.moveThroughTrajectory, 1)
        # self.timer = self.create_timer(0.1, self.move)

def main(args=None):
    rclpy.init(args=args)
    leg = FrontRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
