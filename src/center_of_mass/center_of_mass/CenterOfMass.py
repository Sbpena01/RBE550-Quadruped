import rclpy
from rclpy import time
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

from geometry_msgs.msg import TransformStamped, PoseStamped, Point

"""
Link names (defined in URDF):
[FORMAT EXAMPLE]
[name of the link used to get transform]
    [links whose masses are included to the parent link above]
    # The reason I combine link masses is because (1) many of the links are 'covers' and have the
    # same frame as the link above and (2) it speeds up the calculations.

base_link
    front_link
    rear_link
    imu_link
front_left_shoulder_link
front_left_leg_link
    front_left_leg_link_cover  # THESE ARE MASSLESS
front_left_foot_link
front_left_toe_link
# Repeat for all four legs
"""

class CenterOfMass(Node):
    # Node used the calculate the center of mass of the robot.
    def __init__(self):
        super().__init__("center_of_mass")
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.tf_broadcaster = StaticTransformBroadcaster(self)
        self.timer = self.create_timer(0.5, self.calculateCOM)

        self.links = {
            #            base  front rear   imu
            'base_link': 20.0 + 0.2 + 0.2 + 0.01,

            'front_left_shoulder_link': 0.10,
            'front_left_leg_link': 0.15,
            'front_left_foot_link': 0.1,
            'front_left_toe_link': 0.05,

            'front_right_shoulder_link': 0.10,
            'front_right_leg_link': 0.15,
            'front_right_foot_link': 0.1,
            'front_right_toe_link': 0.05,

            'rear_left_shoulder_link': 0.10,
            'rear_left_leg_link': 0.15,
            'rear_left_foot_link': 0.1,
            'rear_left_toe_link': 0.05,

            'rear_right_shoulder_link': 0.10,
            'rear_right_leg_link': 0.15,
            'rear_right_foot_link': 0.1,
            'rear_right_toe_link': 0.05,
        }
    
    def calculateCOM(self):
        total_mass = 0
        weighted_position = Point()
        for link, mass in self.links.items():
            transform = self.getTransform(link)
            translation = transform.transform.translation

            weighted_position.x += translation.x * mass
            weighted_position.y += translation.y * mass
            weighted_position.z += translation.z * mass

            total_mass += mass
        
        if total_mass > 0:
            com = TransformStamped()
            com.header.stamp = self.get_clock().now().to_msg()
            com.header.frame_id = 'base_link'
            com.child_frame_id = 'center_of_mass'
            com.transform.translation.x = weighted_position.x / total_mass
            com.transform.translation.y = weighted_position.y / total_mass
            com.transform.translation.z = weighted_position.z / total_mass

            # We just want a translation, not a rotation.
            com.transform.rotation.x = 0.0
            com.transform.rotation.y = 0.0
            com.transform.rotation.z = 0.0
            com.transform.rotation.w = 1.0

            self.tf_broadcaster.sendTransform(com)
        else:
            print("No Total Mass")



    def getTransform(self, source:str) -> TransformStamped:
        target = 'base_link'
        print(time.Time())
        try:
            transform = self.tf_buffer.lookup_transform(
                target,
                source,
                time.Time())
            print("Found transform!")
            return transform
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {target} to {source}: {ex}')
            return TransformStamped()

def main(args=None):
    rclpy.init(args=args)
    print('Running...')
    node = CenterOfMass()
    rclpy.spin(node)

if __name__ == '__main__':
    main()