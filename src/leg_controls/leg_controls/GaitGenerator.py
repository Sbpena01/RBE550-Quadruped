#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from custom_interface.msg import LegState


left_pose = Pose()
left_pose.position.x = -30.0
left_pose.position.y = -130.0
left_pose.position.z = -10.0

right_pose = Pose()
right_pose.position.x = -20.0
right_pose.position.y = -130.0
right_pose.position.z = -10.0

default = Pose()
default.position.x = -20.0
default.position.y = -130.0
default.position.z = 10.0

class Gait(Node):
    def __init__(self):
        super().__init__('walking_gait')
        self.fl_publisher = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_publisher = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_publisher = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_publisher = self.create_publisher(LegState, '/rear_right_ee_pose', 10)

        self.fl_pose = left_pose
        self.fr_pose = right_pose
        self.rl_pose = left_pose
        self.rr_pose = right_pose

        self.duty_cycle = 0.5
        self.time = 1
        self.phase = 0
        self.timer = self.create_timer(self.time * self.duty_cycle, self.generateForwardGait)
    
    def generateForwardGait(self):
        # Rear Right, start with trot
        swinging_state = LegState()
        swinging_state.is_swing = True
        swinging_state.pose = default
        stance_state = LegState()
        stance_state.is_swing = False
        stance_state.pose = right_pose
        # self.get_logger().info(f"{self.phase}")
        match self.phase:
            case 0:
                self.rr_publisher.publish(swinging_state)
                self.fl_publisher.publish(stance_state)
                self.rl_publisher.publish(stance_state)
                self.fr_publisher.publish(stance_state)
            case 1:
                self.rr_publisher.publish(stance_state)
                self.fl_publisher.publish(swinging_state)
                self.rl_publisher.publish(stance_state)
                self.fr_publisher.publish(stance_state)
            case 2:
                self.rr_publisher.publish(stance_state)
                self.fl_publisher.publish(stance_state)
                self.rl_publisher.publish(swinging_state)
                self.fr_publisher.publish(stance_state)
            case 3:
                self.rr_publisher.publish(stance_state)
                self.fl_publisher.publish(stance_state)
                self.rl_publisher.publish(stance_state)
                self.fr_publisher.publish(swinging_state)
        self.phase = (self.phase + 1) % 4


def main(args=None):
    rclpy.init(args=args)
    walk = Gait()
    rclpy.spin(walk)
            

if __name__=='__main__':
    main()