import os
import xacro
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.actions import RegisterEventHandler, SetEnvironmentVariable
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Launch Arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default=True)

    # Get path directories of launch files we will use
    robot_description_path = os.path.join(
        get_package_share_directory('robot_description'))
    
    robot_sim_path = os.path.join(
        get_package_share_directory('robot_sim'))

    # Set gazebo sim resource path. Required for gz to find meshes and world file.
    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[
            os.path.join(robot_sim_path, 'worlds'), ':' +
            str(Path(robot_description_path).parent.resolve())
            ]
        )

    # Launch arguement is declared. Used when we want to launch gz with another world file.
    arguments = LaunchDescription([
                DeclareLaunchArgument('world', default_value='robot_world',
                          description='Gz sim World'),
           ]
    )

    # Defines how we want to launch gz.
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch'), '/gz_sim.launch.py']),
                launch_arguments=[
                    ('gz_args', [LaunchConfiguration('world'),  # World file is specified
                                 '.sdf',
                                 ' -v 4',  # set verbosity of gz console output
                                 ' -r']  # Tells gz to run immediately
                    )
                ]
             )

    # Read robot xacro file, defining robot state publisher and spawning robot
    xacro_file = os.path.join(robot_description_path,
                              'robots',
                              'spotmicro_copy.xacro')

    doc = xacro.process_file(xacro_file, mappings={'use_sim' : 'true'})

    robot_desc = doc.toprettyxml(indent='  ')

    params = {'robot_description': robot_desc}
    
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    gz_spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-string', robot_desc,
                   '-x', '0.0',  # Robot's starting position and orientation
                   '-y', '0.0',
                   '-z', '0.5',
                   '-R', '0.0',
                   '-P', '0.0',
                   '-Y', '0.0',
                   '-name', 'robot',
                   '-allow_renaming', 'false'],
    )

    # yaml_file = os.path.join(robot_description_path,
    #                           'config',
    #                           'robot_sim.yaml')

    # controller_manager = Node(
    #     package="controller_manager",
    #     executable="ros2_control_node",
    #     parameters=[params, yaml_file],
    #     output="screen"
    # )

    # ROS2 controllers are activated
    load_joint_state_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'joint_state_broadcaster'],
        output='screen'
    )

    load_front_left_leg_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'front_left_leg_controller'],
        output='screen'
    )

    load_rear_right_leg_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'rear_right_leg_controller'],
        output='screen'
    )

    load_rear_left_leg_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'rear_left_leg_controller'],
        output='screen'
    )

    load_front_right_leg_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
             'front_right_leg_controller'],
        output='screen'
    )

    # Bridge node is defined. We have no lidar so this is commented to be a reference.
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu_data@sensor_msgs/msg/Imu@gz.msgs.IMU'],  # ros_topic@ros2_msg_type@gazebo_msg_type
        output='screen'
    )

    # Define node to start rviz2
    rviz_config_file = os.path.join(robot_description_path, 'config', 'robot_config.rviz')

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    # Launch
    return LaunchDescription([
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=gz_spawn_entity,
                on_exit=[load_joint_state_controller],
            )
        ),
        RegisterEventHandler(
            event_handler=OnProcessExit(
               target_action=load_joint_state_controller,
               on_exit=[load_front_left_leg_controller,
                        load_front_right_leg_controller,
                        load_rear_left_leg_controller,
                        load_rear_right_leg_controller],
            )
        ),
        gazebo_resource_path,
        arguments,
        gazebo,
        node_robot_state_publisher,
        gz_spawn_entity,
        bridge,
        # controller_manager,
        rviz,
    ])
