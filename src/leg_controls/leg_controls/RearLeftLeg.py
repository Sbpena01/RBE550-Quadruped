#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState

class RearLeftLeg(Leg):
    def __init__(self):
        super().__init__('rear_left_leg', is_left=True)
        self.pose_subscriber = self.create_subscription(LegState, '/rear_left_ee_pose', self.moveThroughTrajectory, 1)
        # self.timer = self.create_timer(0.1, self.move)

def main(args=None):
    rclpy.init(args=args)
    leg = RearLeftLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
