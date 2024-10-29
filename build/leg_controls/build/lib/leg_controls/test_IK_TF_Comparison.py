import rclpy
from rclpy.node import Node
from rclpy import time
import asyncio

import rclpy.time
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import Pose

from FrontLeftLeg import FrontLeftLeg  # We want to use the IK method

# The purpose of this script is to compare the values from the TF tree and our IK math.
# We first move a leg (Front Left Leg for no specific reason) to a known pose.
# Then we listen to the TF broadcaster to see what values it is printing.
# This can help understand if there is a relationship between these values
# that can be controlled and implemented into GaitGenerator.


class Comparison(Node):
    def __init__(self):
        super().__init__('comparison_test')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.leg = FrontLeftLeg()
        self.ik_publisher = self.create_publisher(Pose, '/front_left_ee_pose', 10)

        self.transform = None
        self.timer = self.create_timer(0.5, self.new_getTransform)
    
    def __call__(self, pose):
        IK_pose = Pose()
        IK_pose.position.x = pose[0]
        IK_pose.position.y = pose[1]
        IK_pose.position.z = pose[2]
        self.ik_publisher.publish(IK_pose)
        print(IK_pose.position)

        transform = self.new_getTransform('front_left_toe_link', 'front_left_shoulder_link')
        print(transform)

    def getTransform(self, target: str, source: str):
        print(self.get_clock().now())
        print(rclpy.time.Time())
        try:
            future_transform = self.tf_buffer.wait_for_transform_async(
                target,
                source,
                rclpy.time.Time()
            )
            print('Spinning...')
            rclpy.spin_until_future_complete(self, future_transform)
            print('Done!')
            transform = asyncio.run(self.tf_buffer.lookup_transform_async(
                target,
                source,
                rclpy.time.Time()
            ))
            return transform
        except Exception as e:
            self.get_logger().error(f"Could not lookup transform: {e}")
            return None
    
    def new_getTransform(self, target='front_left_shoulder_link', source='front_left_toe_link'):
        print('Running...')
        try:
            self.transform = self.tf_buffer.lookup_transform(
                target,
                source,
                rclpy.time.Time())
            print(self.transform)
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {target} to {source}: {ex}')
            return

def main(args=None):
    rclpy.init(args=args)
    comparison = Comparison()
    pose = [0.0, -110.0, 0.0]
    comparison(pose)
    rclpy.spin(comparison)

if __name__ == '__main__':
    main()