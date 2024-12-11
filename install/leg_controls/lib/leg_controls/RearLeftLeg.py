#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from Leg import Leg
from custom_interface.msg import LegState
from geometry_msgs.msg import Pose
import numpy as np

class RearLeftLeg(Leg):
    def __init__(self):
        super().__init__('rear_left', is_left=True)
        self.pose_subscriber = self.create_subscription(LegState, '/rear_left_ee_pose', self.moveThroughTrajectory, 1)
        rl_state = LegState()
        rl_state.is_swing = False
        rl_state.pose.position.x = 0.1016 + 0.01
        rl_state.pose.position.y = -0.088
        rl_state.pose.position.z = -0.15
        self.home_pose = rl_state.pose
        self.current_pose = rl_state.pose
        self.move()

def main(args=None):
    rclpy.init(args=args)
    leg = RearLeftLeg()
    try:
        rclpy.spin(leg)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
