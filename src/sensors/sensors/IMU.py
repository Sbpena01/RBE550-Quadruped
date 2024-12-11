import rclpy
from rclpy.node import Node

import numpy as np

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from custom_interface.msg import ImuData  # Highlighted as a warning, but ROS2 takes care of it.

class IMU(Node):
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

    def quatToEuler(self, quat:Quaternion):
        x = quat.x
        y = quat.y
        z = quat.z
        w = quat.w

        # Compute roll (rotation around x-axis)
        sinr_cosp = 2.0 * (w * x + y * z)
        cosr_cosp = 1.0 - 2.0 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        # Compute pitch (rotation around y-axis)
        sinp = 2.0 * (w * y - z * x)
        pitch = np.arcsin(np.clip(sinp, -1.0, 1.0))  # Clamp to avoid numerical issues

        # Compute yaw (rotation around z-axis)
        siny_cosp = 2.0 * (w * z + x * y)
        cosy_cosp = 1.0 - 2.0 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw

    def publish(self):
        msg = ImuData()
        msg.roll = self.roll
        msg.pitch = self.pitch
        msg.yaw = self.yaw
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = IMU('imu')
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()