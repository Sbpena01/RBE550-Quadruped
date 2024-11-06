#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from geometry_msgs.msg import Pose

class FrontRightLeg(Leg):
    def __init__(self):
        super().__init__('front_right_leg', is_left=False)
        self.pose_subscriber = self.create_subscription(Pose, '/front_right_ee_pose', self.moveTo, 10)

def main(args=None):
    rclpy.init(args=args)
    leg = FrontRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
