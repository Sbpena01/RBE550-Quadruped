import rclpy
from rclpy.node import Node

import numpy as np

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from custom_interface.srv import ImuData  # Highlighted as a warning, but ROS2 takes care of it.

class IMU(Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)
        self.srv = self.create_service(ImuData, 'get_imu_data', self.callback)
        self.imu_subscriber = self.create_subscription(Imu, '/imu_data', self.update)
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

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

    def callback(self, request, response):
        response.roll = self.roll
        response.pitch = self.pitch
        response.yaw = self.yaw
        return response

def main(args=None):
    rclpy.init(args=args)
    node = IMU('imu')
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()