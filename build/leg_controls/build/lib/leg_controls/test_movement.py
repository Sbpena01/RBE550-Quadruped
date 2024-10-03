#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose

import numpy as np
import time


class FootPoseTest(Node):
    def __init__(self):
        super().__init__('joint_angle_test')
        self.front_left_publisher = self.create_publisher(Pose, '/front_left_ee_pose', 10)
        self.front_rear_publisher = self.create_publisher(Pose,'/front_right_ee_pose', 10)
        self.rear_left_publisher = self.create_publisher(Pose,'/rear_left_ee_pose', 10)
        self.rear_rear_publisher = self.create_publisher(Pose,'/rear_right_ee_pose', 10)
    
    def runTest(self):
        steps = np.linspace(-70.0, -150.0, 18)
        x = 0.0
        z = 0.0
        for step in steps:
            pose_to_be_published = Pose()
            pose_to_be_published.position.x = x
            pose_to_be_published.position.y = step
            pose_to_be_published.position.z = z

            self.front_left_publisher.publish(pose_to_be_published)
            self.front_rear_publisher.publish(pose_to_be_published)
            self.rear_left_publisher.publish(pose_to_be_published)
            self.rear_rear_publisher.publish(pose_to_be_published)

            time.sleep(1)  # 1 Hz

def main(args=None):
    rclpy.init(args=args)
    test = FootPoseTest()
    while True:
        test.runTest()
        time.sleep(0.1)

if __name__ == '__main__':
    main()