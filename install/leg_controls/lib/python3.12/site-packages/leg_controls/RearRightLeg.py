#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from geometry_msgs.msg import Pose

class RearRightLeg(Leg):
    def __init__(self):
        super().__init__('rear_right_leg', is_left=False)
        self.pose_subscriber = self.create_subscription(Pose, '/rear_right_ee_pose', self.moveTo, 10)

def main(args=None):
    rclpy.init(args=args)
    rear_right_leg = RearRightLeg()
    try:
        rclpy.spin(rear_right_leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
