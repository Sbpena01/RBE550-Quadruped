from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import RegisterEventHandler, SetEnvironmentVariable
from launch.event_handlers import OnProcessExit, OnProcessStart

def generate_launch_description():

    map = Node(package='motion_planner', executable='map', output='screen')
    rrt = Node(package='motion_planner', executable='rrt', output='screen')
    imu = Node(package='sensors', executable='imu', output='screen')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        map, rrt, imu
    ])