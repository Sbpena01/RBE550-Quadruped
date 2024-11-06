import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
import time

class LegInit(Node):
    init_pose = Pose()
    init_pose.position.x = -30.0
    init_pose.position.y = -130.0
    init_pose.position.z = -10.0

    def __init__(self, node_name:str):
        super().__init__(node_name)
        self.fl_pub = self.create_publisher(Pose, '/front_left_ee_pose', 10)
        self.fr_pub = self.create_publisher(Pose, '/front_right_ee_pose', 10)
        self.rl_pub = self.create_publisher(Pose, '/rear_left_ee_pose', 10)
        self.rr_pub = self.create_publisher(Pose, '/rear_right_ee_pose', 10)

    def initLegs(self):
        self.fl_pub.publish(self.init_pose)
        self.fr_pub.publish(self.init_pose)
        self.rl_pub.publish(self.init_pose)
        self.rr_pub.publish(self.init_pose)


def main(args=None):
    rclpy.init(args=args)
    node = LegInit('leg_init')
    time.sleep(1)
    node.initLegs()
    rclpy.shutdown()


if __name__ == '__main__':
    main()