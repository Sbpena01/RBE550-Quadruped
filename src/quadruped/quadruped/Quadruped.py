import ikpy.chain
import rclpy
import ikpy
from rclpy import time
from rclpy.node import Node

from custom_interface.msg import LegState

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import TransformStamped, Pose

class Quadruped(Node):
    def __init__(self):
        super().__init__('quadruped')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        # LegState Publishers to command legs to go to specific poses
        self.fl_pub = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_pub = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_pub = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_pub = self.create_publisher(LegState, '/rear_right_ee_pose', 10)
        self.legs = self.init_states()
        self.timer = self.create_timer(0.1, self.updateStates)

    def init_states(self):
        fl_state = LegState()
        fl_state.is_swing = False
        fl_state.pose.position.x = 0.1016
        fl_state.pose.position.y = -0.088
        fl_state.pose.position.z = -0.15
        self.fl_pub.publish(fl_state)

        fr_state = LegState()
        fr_state.is_swing = False
        fr_state.pose.position.x = 0.1016
        fr_state.pose.position.y = 0.088
        fr_state.pose.position.z = -0.15
        self.fr_pub.publish(fr_state)

        rl_state = LegState()
        rl_state.is_swing = False
        rl_state.pose.position.x = -0.0844
        rl_state.pose.position.y = -0.088
        rl_state.pose.position.z = -0.15
        self.rl_pub.publish(rl_state)

        rr_state = LegState()
        rr_state.is_swing = False
        rr_state.pose.position.x = -0.0844
        rr_state.pose.position.y = 0.088
        rr_state.pose.position.z = -0.15
        self.rr_pub.publish(rr_state)
        return {
            'front_left': [fl_state, self.fl_pub],
            'front_right': [fr_state, self.fr_pub],
            'rear_left': [rl_state, self.rl_pub],
            'rear_right': [rr_state, self.rr_pub]
        }
    
    def swingLegTo(self, leg:str, pose:Pose):
        state = LegState()
        state.is_swing = True
        state.pose = pose
        self.legs[leg][1].publish(state)

    def updateStates(self):
        for leg in self.legs.keys():
            new_state = LegState()
            new_state.is_swing = False
            transform = self.getTransform(leg)
            leg_pose = Pose()
            leg_pose.position.x = transform.transform.translation.x
            leg_pose.position.y = transform.transform.translation.y
            leg_pose.position.z = transform.transform.translation.z
            new_state.pose = leg_pose
            self.legs[leg][0] = new_state


    def calculateSupportPolygon(self):
        # First, we need to know which legs are contacting the ground.
        contact_legs = []
        for leg, item in self.legs.items():
            state: LegState = item[0]
            if not state.is_swing:
                contact_legs.append(leg)

        x_coords = []
        y_coords = []
        for leg in contact_legs:
            pose = self.legs[leg][0].pose.position
            x_coords.append(pose.x)
            y_coords.append(pose.y)


    def getTransform(self, source: str) -> TransformStamped:
        target = 'base_link'
        try:
            transform = self.tf_buffer.lookup_transform(
                target,
                source+"_toe_link",
                time.Time())
            return transform
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {target} to {source}: {ex}')
            return TransformStamped()


def main(args=None):
    rclpy.init(args=args)
    node = Quadruped()
    node.calculateSupportPolygon()
    input("Ready?")
    pose = Pose()
    pose.position.x = 0.1016 + 0.02
    pose.position.y = -0.088
    pose.position.z = -0.15
    node.swingLegTo("front_left", pose)
    rclpy.spin(node)

if __name__ == '__main__':
    main()