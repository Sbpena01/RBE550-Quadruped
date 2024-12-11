# RBE550-

Welcome to our RBE 550 Semester Project! This code was built using ROS2 Jazzy and Ubuntu 24.04. Other ROS2 versions and Ubuntu versions may not be compatible. Below are the series of terminal commands you will need to run to demonstrate our project. After cloning this repository, be sure to run `colcon build` within the RBE550-Quadruped directory. Make sure you have sourced both /opt/ros/jazzy/setup.bash and install/setup.bash (or bash.rc if you have that set up).
## If you get an error regarding __pycache__ when building
Run these commands depending on what is erroring:
`rm -r src/robot_sim/launch/__pycache__/` or `rm -r src/robot_sim/worlds/__pycache__/`. It is always one of these two and we aren't sure why this is a problem or how to fix it. However, after deleting this, the code will build just fine.

# Launching Gazebo and RViz
Simply run `ros2 launch robot_sim robot_spawn_launch.py`
Wait until nothing is printing to the terminal before moving on to the next step. If you see that a controller has not loaded, retry the command.
This will launch both Gazebo and RViz.

# Launching the Leg Control Nodes
This is responsible for activating the controllers for each leg in the quadruped. Run `ros2 launch leg_controls leg_controls_launch.py`. Sometimes, the legs will not init at the same time, so the robot will fall. If this happens, feel free to use the Gazebo manipulation tools (seen in the top left corner) to re-orient Spot on his feet. 

# Running the Gait Scripts
By running `ros2 run quadruped quaruped <gait_type>`, you will see that Spot begins to do the gait that is chosen in `<gait_type>`. The options are 'walk', 'turn_left'. and 'turn_right'. Technically, 'stop' is an option, but it is not very eventful.

# Running the RRT
`ros2 launch motion_planner mapping_launch.py` will launch the rrt demo and publish the map to RViz.
