import rclpy
from rclpy.node import Node
from custom_interface.msg import LegState
import time

class LegInit(Node):
    left_pose = LegState()
    left_pose.is_swing = False
    left_pose.pose.position.x = -30.0
    left_pose.pose.position.y = -130.0
    left_pose.pose.position.z = -10.0

    right_pose = LegState()
    right_pose.is_swing = False
    right_pose.pose.position.x = -20.0
    right_pose.pose.position.y = -130.0
    right_pose.pose.position.z = -10.0

    def __init__(self, node_name:str):
        super().__init__(node_name)
        self.fl_pub = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_pub = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_pub = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_pub = self.create_publisher(LegState, '/rear_right_ee_pose', 10)

    def initLegs(self):
        self.fl_pub.publish(self.left_pose)
        self.fr_pub.publish(self.right_pose)
        self.rl_pub.publish(self.left_pose)
        self.rr_pub.publish(self.right_pose)


def main(args=None):
    rclpy.init(args=args)
    node = LegInit('leg_init')
    time.sleep(3)
    node.initLegs()
    rclpy.shutdown()


if __name__ == '__main__':
    main()