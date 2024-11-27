#/usr/bin/env python3
import ikpy.chain
import ikpy.urdf
import ikpy.urdf.URDF
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState
from ikpy import chain
from ikpy.link import OriginLink, URDFLink

class RearRightLeg(Leg):
    def __init__(self):
        super().__init__('rear_right', is_left=False)
        self.pose_subscriber = self.create_subscription(LegState, '/rear_right_ee_pose', self.moveThroughTrajectory, 10)

def main(args=None):
    rclpy.init(args=args)
    leg = RearRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
