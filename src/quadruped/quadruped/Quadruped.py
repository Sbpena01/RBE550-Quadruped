import time as t
import rclpy
import ikpy
from rclpy import time
from rclpy.node import Node

from custom_interface.msg import ImuData, LegState

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
        self.legs: dict = None
        self.init_states()
        self.timer = self.create_timer(0.1, self.updateStates)

        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.updateOffsets, 1)
        self.imu_data = None
        self.x_offset = 0.0
        self.y_offset = 0.0

    def init_states(self):
        fl_state = LegState()
        fl_state.is_swing = False
        fl_state.pose.position.x = -0.0844
        fl_state.pose.position.y = -0.088
        fl_state.pose.position.z = -0.15

        fr_state = LegState()
        fr_state.is_swing = False
        fr_state.pose.position.x = -0.0844
        fr_state.pose.position.y = 0.088
        fr_state.pose.position.z = -0.15

        rl_state = LegState()
        rl_state.is_swing = False
        rl_state.pose.position.x = 0.1016
        rl_state.pose.position.y = -0.088
        rl_state.pose.position.z = -0.15

        rr_state = LegState()
        rr_state.is_swing = False
        rr_state.pose.position.x = 0.1016
        rr_state.pose.position.y = 0.088
        rr_state.pose.position.z = -0.15

        self.legs = {
            'front_left': [fl_state, self.fl_pub],
            'front_right': [fr_state, self.fr_pub],
            'rear_left': [rl_state, self.rl_pub],
            'rear_right': [rr_state, self.rr_pub]
        }
        # self.fl_pub.publish(fl_state)
        # self.fr_pub.publish(fr_state)
        # self.rl_pub.publish(rl_state)
        # self.rr_pub.publish(rr_state)
        self.moveLegTo('front_left', fl_state.pose)
        self.moveLegTo('front_right', fr_state.pose)
        self.moveLegTo('rear_left', rl_state.pose)
        self.moveLegTo('rear_right', rr_state.pose)
    
    def moveLegTo(self, leg:str, pose:Pose):
        state = LegState()
        state.is_swing = False
        state.pose = pose
        self.legs[leg][1].publish(state)

    def swingLegTo(self, leg:str, pose:Pose):
        state = LegState()
        state.is_swing = True
        state.pose = pose
        self.legs[leg][1].publish(state)

    def test_swingLegTo(self, leg:str):
        state = LegState()
        state.is_swing = True
        pose = self.legs[leg][0].pose
        pose.position.x += -0.1
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

    def getContactLegs(self):
        contact_legs = []
        for leg, item in self.legs.items():
            state: LegState = item[0]
            if not state.is_swing:
                contact_legs.append(leg)
        return contact_legs

    def calculateSupportPolygon(self):
        # First, we need to know which legs are contacting the ground.
        contact_legs = self.getContactLegs()

        x_coords = []
        y_coords = []
        for leg in contact_legs:
            pose = self.legs[leg][0].pose.position
            x_coords.append(pose.x)
            y_coords.append(pose.y)

    def stability(self):
        # First, we need to know which legs are contacting the ground.
        contact_legs = self.getContactLegs()
        for leg in contact_legs:
            current_pose: Pose = self.legs[leg][0].pose
            new_pose = Pose()
            new_pose.position.x = current_pose.position.x
            new_pose.position.y = current_pose.position.y
            new_pose.position.z = current_pose.position.z
            if leg == 'rear_left':
                self.get_logger().info(f"Offsets: {self.x_offset}. Curr: {current_pose.position.x}. New: {new_pose.position.x} ")

            # self.moveLegTo(leg, new_pose)

    def updateOffsets(self, imu_data: ImuData):
        # k_x = 0.1
        # k_y = 1.0
        # self.x_offset = k_x * -imu_data.pitch
        # self.y_offset = k_y * imu_data.pitch
        self.stability()

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
    t.sleep(3)
    node.test_swingLegTo('front_left')
    t.sleep(3)
    node.test_swingLegTo('front_right')
    t.sleep(3)
    node.test_swingLegTo('rear_left')
    t.sleep(3)
    node.test_swingLegTo('rear_right')
    rclpy.spin(node)

if __name__ == '__main__':
    main()