from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import RegisterEventHandler, SetEnvironmentVariable
from launch.event_handlers import OnProcessExit, OnProcessStart

def generate_launch_description():

    leg_control_path = os.path.join(
        get_package_share_directory('leg_controls'))

    front_left_leg = Node(package='leg_controls', executable='FrontLeftLeg', output='screen')
    front_right_leg = Node(package='leg_controls', executable='FrontRightLeg', output='screen')
    rear_left_leg = Node(package='leg_controls', executable='RearLeftLeg', output='screen')
    rear_right_leg = Node(package='leg_controls', executable='RearRightLeg', output='screen')
    init_legs = Node(package='leg_controls', executable='leg_init', output='screen', )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        front_left_leg,
        front_right_leg,
        rear_right_leg,
        rear_left_leg,
        init_legs
    ])