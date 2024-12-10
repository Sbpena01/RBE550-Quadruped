import rclpy
import time as t
from rclpy import time
from rclpy.node import Node

from custom_interface.msg import ImuData, LegState

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import TransformStamped, Pose, PolygonStamped, Point32
from ros_gz_interfaces.msg import Contact

class Quadruped(Node):
    def __init__(self):
        super().__init__('quadruped')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        # Publishers
        self.fl_pub = self.create_publisher(LegState, '/front_left_ee_pose', 10)
        self.fr_pub = self.create_publisher(LegState, '/front_right_ee_pose', 10)
        self.rl_pub = self.create_publisher(LegState, '/rear_left_ee_pose', 10)
        self.rr_pub = self.create_publisher(LegState, '/rear_right_ee_pose', 10)
        self.support_polygon_visualization = self.create_publisher(PolygonStamped, '/support_polygon', 10)

        self.fl_sub = self.create_subscription(LegState, '/front_left_leg_state', self.updateStates, 10)
        self.fr_sub = self.create_subscription(LegState, '/front_right_leg_state', self.updateStates, 10)
        self.rl_sub = self.create_subscription(LegState, '/rear_left_leg_state', self.updateStates, 10)
        self.rr_sub = self.create_subscription(LegState, '/rear_right_leg_state', self.updateStates, 10)
        self.legs: dict = None
        self.is_initiated = False
        self.init_states()
        self.leg_timer = self.create_timer(0.75, self.step_leg)
        self.leg_count = 0

        # Prefered poses to step to:
        self.fl_step = Pose()
        self.fl_step.position.x = -0.0844 - 0.05
        self.fl_step.position.y = -0.088
        self.fl_step.position.z = -0.15

        self.fr_step = Pose()
        self.fr_step.position.x = -0.0844 - 0.05
        self.fr_step.position.y = 0.088
        self.fr_step.position.z = -0.15

        self.rl_step = Pose()
        self.rl_step.position.x = 0.1016 - 0.05
        self.rl_step.position.y = -0.088
        self.rl_step.position.z = -0.15

        self.rr_step = Pose()
        self.rr_step.position.x = 0.1016 - 0.05
        self.rr_step.position.y = 0.088
        self.rr_step.position.z = -0.15

        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.updateOffsets, 1)
        self.imu_data = None
        self.x_offset = 0.0
        self.y_offset = 0.0

    def step_leg(self):
        if not self.is_initiated:
            return
        self.leg_count = self.leg_count % 6
        match self.leg_count:
            case 0:
                self.swingLegTo('rear_left', self.rl_step)
                self.leg_count += 1
            case 1:
                self.swingLegTo('front_left', self.fl_step)
                self.leg_count += 1
            case 2:
                self.moveAllLegsBack(0.035)
                self.leg_count += 1
            case 3:
                self.swingLegTo('rear_right', self.rr_step)
                self.leg_count += 1
            case 4:
                self.swingLegTo('front_right', self.fr_step)
                self.leg_count += 1
            case 5:
                self.moveAllLegsBack(0.035)
                self.leg_count += 1

    def init_states(self):
        fl_state = LegState()
        fl_state.is_swing = False
        fl_state.pose.position.x = -0.0844 - 0.01
        fl_state.pose.position.y = -0.088
        fl_state.pose.position.z = -0.15

        fr_state = LegState()
        fr_state.is_swing = False
        fr_state.pose.position.x = -0.0844 - 0.01
        fr_state.pose.position.y = 0.088
        fr_state.pose.position.z = -0.15

        rl_state = LegState()
        rl_state.is_swing = False
        rl_state.pose.position.x = 0.1016 + 0.01
        rl_state.pose.position.y = -0.088
        rl_state.pose.position.z = -0.15

        rr_state = LegState()
        rr_state.is_swing = False
        rr_state.pose.position.x = 0.1016 + 0.01
        rr_state.pose.position.y = 0.088
        rr_state.pose.position.z = -0.15

        self.legs = {
            'front_left': [fl_state, self.fl_pub],
            'front_right': [fr_state, self.fr_pub],
            'rear_right': [rr_state, self.rr_pub],
            'rear_left': [rl_state, self.rl_pub]
        }
        self.moveLegTo('front_left', fl_state.pose)
        self.moveLegTo('front_right', fr_state.pose)
        self.moveLegTo('rear_left', rl_state.pose)
        self.moveLegTo('rear_right', rr_state.pose)
        t.sleep(0.5)
        self.is_initiated = True
    
    def moveLegTo(self, leg:str, pose:Pose):
        state = LegState()
        state.is_swing = False
        state.pose = pose
        self.legs[leg][1].publish(state)

    def moveAllLegsBack(self, distance):
        for leg in self.legs.keys():
            state = LegState()
            state.is_swing = False
            pose = self.legs[leg][0].pose
            pose.position.x += distance
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
        pose.position.x += -0.05
        state.pose = pose
        self.legs[leg][1].publish(state)

    def updateStates(self, msg:LegState):
        leg = msg.name
        self.legs[leg][0] = msg
        self.get_logger().info(f"Leg: {leg} Z: {self.legs[leg][0].pose.position.z}")

    def getContactLegs(self):
        contact_legs = []
        for leg, item in self.legs.items():
            state: LegState = item[0]
            if not state.is_swing:
                contact_legs.append(leg)
        return contact_legs

    def calculateSupportPolygon(self, contact_legs, visualize=True):
        # First, we need to know which legs are contacting the ground.
        x_coords = []
        y_coords = []
        z_coords = []
        for leg in contact_legs:
            pose = self.legs[leg][0].pose.position
            x_coords.append(pose.x)
            y_coords.append(pose.y)
            z_coords.append(pose.z)
        if visualize:
            polygon = PolygonStamped()
            polygon.header.frame_id = 'base_link'
            polygon.header.stamp = time.Time().to_msg()
            points: list[Point32] = []
            for idx in range(len(x_coords)):
                point = Point32()
                point.x = x_coords[idx]
                point.y = y_coords[idx]
                point.z = z_coords[idx]
                points.append(point)
            polygon.polygon.points = points
            self.support_polygon_visualization.publish(polygon)
        return x_coords, y_coords

    def findCenter(self, x_coords, y_coords):
        # Check that the lengths of x_coords and y_coords match
        if len(x_coords) != len(y_coords):
            raise ValueError("x_coords and y_coords must have the same length")
        
        # Calculate the centroid (center) of the polygon
        x_center = sum(x_coords) / len(x_coords)
        y_center = sum(y_coords) / len(y_coords)
        
        return (x_center, y_center)

    def stability(self):
        if not self.is_initiated:
            return
        contact_legs = self.getContactLegs()
        sp_x, sp_y = self.calculateSupportPolygon(contact_legs)
        support_polygon_center = self.findCenter(sp_x, sp_y)
        com_transform = self.getTransform('center_of_mass')
        x_error = support_polygon_center[0] - com_transform.transform.translation.x
        y_error = support_polygon_center[1] - com_transform.transform.translation.y
        # self.get_logger().info(f"X_error: {x_error}. Y_error: {y_error}.")
        # for leg in contact_legs:
        #     current_pose: Pose = self.legs[leg][0].pose
        #     new_pose = Pose()
        #     new_pose.position.x = current_pose.position.x - x_error
        #     new_pose.position.y = current_pose.position.y + y_error 
        #     new_pose.position.z = current_pose.position.z
        #     self.moveLegTo(leg, new_pose)

    def updateOffsets(self, imu_data: ImuData):
        k_x = 0.1
        k_y = 0.1
        self.x_offset = k_x * -imu_data.pitch
        self.y_offset = k_y * imu_data.pitch
        self.stability()

    def getTransform(self, source: str) -> TransformStamped:
        target = 'base_link'
        try:
            transform = self.tf_buffer.lookup_transform(
                target,
                source,
                time.Time())
            return transform
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {target} to {source}: {ex}')
            return TransformStamped()


def main(args=None):
    rclpy.init(args=args)
    node = Quadruped()
    rclpy.spin(node)

if __name__ == '__main__':
    main()