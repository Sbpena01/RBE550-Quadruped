import rclpy
from rclpy.node import Node

import numpy as np

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from custom_interface.msg import ImuData  # Highlighted as a warning, but ROS2 takes care of it.

class ContactSensor(Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)
        self.publisher = self.create_publisher(ImuData, '/get_imu_data', 1)
        self.imu_subscriber = self.create_subscription(Imu, '/imu_data', self.update, 1)
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0
        self.timer = self.create_timer(0.1, self.publish)

    def update(self, imu_data: Imu):
        quat = imu_data.orientation
        self.roll, self.pitch, self.yaw = self.quatToEuler(quat)

    def publish(self):
        self.get_logger().info(f"Publishing: {self.roll}, {self.pitch}, {self.yaw}")
        msg = ImuData()
        msg.roll = self.roll
        msg.pitch = self.pitch
        msg.yaw = self.yaw
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ContactSensor('contact_sensor')
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()