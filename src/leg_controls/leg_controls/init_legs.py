import rclpy
from rclpy.node import Node
from custom_interface.msg import LegState
import time

# DEPERCATED. LEGS ARE INIT WHEN QUADRUPED.PY IS RUN

class LegInit(Node):
    fl_pose = LegState()
    fl_pose.is_swing = False
    fl_pose.pose.position.x = 0.1016
    fl_pose.pose.position.y = -0.088
    fl_pose.pose.position.z = -0.15

    fr_pose = LegState()
    fr_pose.is_swing = False
    fr_pose.pose.position.x = 0.1016
    fr_pose.pose.position.y = 0.088
    fr_pose.pose.position.z = -0.15

    rl_pose = LegState()
    rl_pose.is_swing = False
    rl_pose.pose.position.x = -0.0844
    rl_pose.pose.position.y = -0.088
    rl_pose.pose.position.z = -0.15

    rr_pose = LegState()
    rr_pose.is_swing = False
    rr_pose.pose.position.x = -0.0844
    rr_pose.pose.position.y = 0.088
    rr_pose.pose.position.z = -0.15

    def __init__(self, node_name:str):
        super().__init__(node_name)
        self.fl_pub = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_pub = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_pub = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_pub = self.create_publisher(LegState, '/rear_right_ee_pose', 10)

    def initLegs(self):
        self.fl_pub.publish(self.fl_pose)
        self.fr_pub.publish(self.fr_pose)
        self.rl_pub.publish(self.rl_pose)
        self.rr_pub.publish(self.rr_pose)


def main(args=None):
    rclpy.init(args=args)
    node = LegInit('leg_init')
    # time.sleep(3)
    # node.initLegs()
    rclpy.shutdown()


if __name__ == '__main__':
    main()