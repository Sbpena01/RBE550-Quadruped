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
        rr_state = LegState()
        rr_state.is_swing = False
        rr_state.pose.position.x = 0.1016 + 0.01
        rr_state.pose.position.y = 0.088
        rr_state.pose.position.z = -0.15
        self.current_pose = rr_state.pose
        self.move()

def main(args=None):
    rclpy.init(args=args)
    leg = RearRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
