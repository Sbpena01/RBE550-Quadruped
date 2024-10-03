#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Pose

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

import time
import asyncio

class WalkingGait(Node):
    def __init__(self):
        super().__init__('walking_gait')
        self.left_leg_pose_publisher = self.create_publisher(Pose, '/front_left_ee_pose', 10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
    
    
    
    def getTransform(self, target: str, source: str):
        try:
            future_transform = self.tf_buffer.wait_for_transform_async(
                target,
                source,
                rclpy.time.Time(),
            )

            rclpy.spin_until_future_complete(self, future_transform)

            transform = asyncio.run(self.tf_buffer.lookup_transform_async(
                target,
                source,
                rclpy.time.Time(),
            ))
            return transform
        except Exception as e:
            self.get_logger().error(f"Could not lookup transform: {e}")
            return None


def main(args=None):
    rclpy.init(args=args)
    walking_gait = WalkingGait()
    while rclpy.ok():
        transform = walking_gait.getTransform("front_left_shoulder_link", "front_left_toe_link")
        if transform:
            print(transform)
        rclpy.spin_once(walking_gait)
    rclpy.shutdown()

if __name__=='__main__':
    main()