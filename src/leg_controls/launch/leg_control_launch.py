from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        # Node(package = "joy",executable = "joy_node"),
        Node(package='leg_controls', executable='FrontLeftLeg.py', output='screen'),
    ])