#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from custom_interface.msg import LegState

default = Pose()
default.position.x = -20.0
default.position.y = -130.0
default.position.z = 10.0

stance_1 = Pose()
stance_1.position.x = -20.0
stance_1.position.y = -130.0
stance_1.position.z = 0.0

stance_2 = Pose()
stance_2.position.x = -20.0
stance_2.position.y = -130.0
stance_2.position.z = -10.0

init_pose = Pose()
init_pose.position.x = -20.0
init_pose.position.y = -130.0
init_pose.position.z = -20.0

class Gait(Node):
    def __init__(self):
        super().__init__('walking_gait')
        self.fl_publisher = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_publisher = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_publisher = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_publisher = self.create_publisher(LegState, '/rear_right_ee_pose', 10)

        self.fl_pose = init_pose
        self.fr_pose = init_pose
        self.rl_pose = init_pose
        self.rr_pose = init_pose

        self.duty_cycle = 0.75
        self.time = 4
        self.phase = 0
        self.timer = self.create_timer(self.time * self.duty_cycle, self.generateForwardGait)
    
    def generateForwardGait(self):
        # Rear Right, start with trot
        swinging_state = LegState()
        swinging_state.is_swing = True
        swinging_state.pose = default

        stance_state_1 = LegState()
        stance_state_1.is_swing = False
        stance_state_1.pose = stance_1

        stance_state_2 = LegState()
        stance_state_2.is_swing = False
        stance_state_2.pose = stance_2

        stance_state_3 = LegState()
        stance_state_3.is_swing = False
        stance_state_3.pose = init_pose

        match self.phase:
            case 0:
                self.rr_publisher.publish(swinging_state)
                self.fl_publisher.publish(stance_state_3)
                self.rl_publisher.publish(stance_state_2)
                self.fr_publisher.publish(stance_state_1)
            case 1:
                self.rr_publisher.publish(stance_state_1)
                self.fl_publisher.publish(swinging_state)
                self.rl_publisher.publish(stance_state_3)
                self.fr_publisher.publish(stance_state_2)
            case 2:
                self.rr_publisher.publish(stance_state_2)
                self.fl_publisher.publish(stance_state_1)
                self.rl_publisher.publish(swinging_state)
                self.fr_publisher.publish(stance_state_3)
            case 3:
                self.rr_publisher.publish(stance_state_3)
                self.fl_publisher.publish(stance_state_2)
                self.rl_publisher.publish(stance_state_1)
                self.fr_publisher.publish(swinging_state)
        self.phase = (self.phase + 1) % 4


def main(args=None):
    rclpy.init(args=args)
    walk = Gait()
    rclpy.spin(walk)
            

if __name__=='__main__':
    main()