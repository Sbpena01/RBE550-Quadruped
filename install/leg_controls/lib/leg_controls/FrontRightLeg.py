#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState
from geometry_msgs.msg import Pose
from ikpy import chain
from ikpy.link import OriginLink, URDFLink

class FrontRightLeg(Leg):
    def __init__(self):
        super().__init__('front_right', is_left=False)
        self.pose_subscriber = self.create_subscription(LegState, '/front_right_ee_pose', self.moveThroughTrajectory, 1)
        fr_state = LegState()
        fr_state.is_swing = False
        fr_state.pose.position.x = -0.0844 - 0.01
        fr_state.pose.position.y = 0.088
        fr_state.pose.position.z = -0.15
        self.home_pose = fr_state.pose
        self.current_pose = fr_state.pose
        self.move()

def main(args=None):
    rclpy.init(args=args)
    leg = FrontRightLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
