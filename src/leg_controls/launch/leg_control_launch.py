from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    leg_control_path = os.path.join(
        get_package_share_directory('leg_controls'))

    front_left_leg_control = Node(
        package='leg_controls',
        executable='FrontLeftLeg',
        name='FrontLeftLeg',
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        front_left_leg_control,
        Node(package='leg_controls', executable='FrontRightLeg', output='screen'),
        Node(package='leg_controls', executable='RearLeftLeg', output='screen'),
        Node(package='leg_controls', executable='RearRightLeg', output='screen'),
    ])