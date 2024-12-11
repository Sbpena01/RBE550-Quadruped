import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, TransformStamped, Pose
from rclpy import time
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster


class Map(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.gazebo_subscriber = self.create_subscription(PoseArray, '/world/default/pose/info', self.callback, 10)
        self.tf_broadcaster = StaticTransformBroadcaster(self)

    def callback(self, msg):
        robot_pose : Pose = msg.poses[1]
        odom = TransformStamped()
        odom.transform.translation.x = robot_pose.position.x
        odom.transform.translation.y = robot_pose.position.y
        odom.transform.translation.z = robot_pose.position.z
        odom.transform.rotation.x = robot_pose.orientation.x
        odom.transform.rotation.y = robot_pose.orientation.y
        odom.transform.rotation.z = robot_pose.orientation.z
        odom.transform.rotation.w = robot_pose.orientation.w
        odom.header.frame_id = 'base_link'
        odom.child_frame_id = 'odom'
        odom.header.stamp = time.Time().to_msg()
        self.tf_broadcaster.sendTransform(odom)
        self.get_logger().info(f"{robot_pose}")

def main():
    rclpy.init()
    node = Map('map')
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
