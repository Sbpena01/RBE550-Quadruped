import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, TransformStamped, Pose, Quaternion
from custom_interface.msg import ImuData
from rclpy import time
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import numpy as np


# Map class that keeps track of the world pose for usage of global coordinates
class Map(Node):
    # Initializes node, creates subscribers, and initializes needed variables
    def __init__(self, node_name):
        super().__init__(node_name)
        self.gazebo_subscriber = self.create_subscription(PoseArray, '/world/default/pose/info', self.callback, 10)
        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.updateImu, 10)
        self.tf_broadcaster = StaticTransformBroadcaster(self)
        self.odom2base = TransformStamped()
        self.odom2base.header.frame_id = 'base_link'
        self.odom2base.child_frame_id = 'odom'
        self.map2odom = TransformStamped()
        self.map2odom.header.frame_id = 'odom'
        self.map2odom.child_frame_id = 'map'
        self.timer = self.create_timer(0.1, self.send_transform)

    # Converts the ImuData to quaternion and then updates self rotation values
    def updateImu(self, msg: ImuData):
        q = self.eulerToQuaternion(msg.roll, msg.pitch, msg.yaw)
        self.odom2base.transform.rotation.x = q.x
        self.odom2base.transform.rotation.y = q.y
        self.odom2base.transform.rotation.z = q.z
        self.odom2base.transform.rotation.w = q.w
        self.get_logger().info(f"{q}")

    # Sends transforms of odom, base, and map through broadcasters
    def send_transform(self):
        self.tf_broadcaster.sendTransform(self.odom2base)
        self.tf_broadcaster.sendTransform(self.map2odom)

    # Function that updates the position of the world
    def callback(self, msg):
        robot_pose : Pose = msg.poses[1]
        self.map2odom.transform.translation.x = -robot_pose.position.x
        self.map2odom.transform.translation.y = -robot_pose.position.y
        self.map2odom.transform.translation.z = -robot_pose.position.z
        self.map2odom.header.stamp = time.Time().to_msg()

    # Converts euler angles to quaternions
    def eulerToQuaternion(self, roll, pitch, yaw):
        cy = np.cos(yaw * 0.5)
        sy = np.sin(yaw * 0.5)
        cp = np.cos(pitch * 0.5)
        sp = np.sin(pitch * 0.5)
        cr = np.cos(roll * 0.5)
        sr = np.sin(roll * 0.5)

        q = Quaternion()
        q.w = cr * cp * cy + sr * sp * sy
        q.x = sr * cp * cy - cr * sp * sy
        q.y = cr * sp * cy + sr * cp * sy
        q.z = cr * cp * sy - sr * sp * cy
        return q

# Main function that starts the node
def main():
    rclpy.init()
    node = Map('map')
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == "__main__":
    main()