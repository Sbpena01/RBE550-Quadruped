import rclpy
import time as t
from rclpy import time
from rclpy.node import Node
import numpy as np
import sys

from custom_interface.msg import ImuData, LegState

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import TransformStamped, Pose, PolygonStamped, Point32, Quaternion
from std_msgs.msg import String
from ros_gz_interfaces.msg import Contact
import yaml

class Quadruped(Node):
    def __init__(self, state='walk'):
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

        self.command_sub = self.create_subscription(String, '/quadruped_command', self.changeState, 10)
        self.imu_subscriber = self.create_subscription(ImuData, '/get_imu_data', self.imuCallback, 10)

        self.legs: dict = None
        self.is_initiated = False
        self.init_states()
        self.leg_timer = self.create_timer(0.75, self.move)
        self.leg_count = 0
        self.state = state

        # Prefered poses
        self.walking_poses = self.loadPosesFromYaml('walking_poses')
        self.turn_left_poses = self.loadPosesFromYaml('left_turn_poses')
        self.turn_right_poses = self.loadPosesFromYaml('right_turn_poses')

        self.robot_pose = Pose()
        self.pose_timer = self.create_timer(0.1, self.updateRobotPose)

        self.imu_data:ImuData = ImuData()

    def updateRobotPose(self):
        transform = self.getTransform('base_link', target='map')
        self.robot_pose.position.x = transform.transform.translation.x
        self.robot_pose.position.y = transform.transform.translation.y
        self.robot_pose.position.z = transform.transform.translation.z
        self.robot_pose.orientation.x = transform.transform.rotation.x
        self.robot_pose.orientation.y = transform.transform.rotation.y
        self.robot_pose.orientation.z = transform.transform.rotation.z
        self.robot_pose.orientation.w = transform.transform.rotation.w

        contact_legs = self.getContactLegs()
        self.calculateSupportPolygon(contact_legs)
    
    def imuCallback(self, msg):
        self.imu_data = msg

    def loadPosesFromYaml(self, req: str):
        filepath = "src/quadruped/quadruped/poses.yaml"
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        poses = {}
        for pose_data in data[req]:
            pose = Pose()
            pose.position.x = pose_data['position']['x']
            pose.position.y = pose_data['position']['y']
            pose.position.z = pose_data['position']['z']
            poses[pose_data['name']] = pose
        return poses

    def changeState(self, msg: String):
        self.leg_count = 0
        self.state = msg.data

    def move(self):
        match self.state:
            case 'walk':
                self.step_leg()
            case 'stop':
                self.stop()
            case 'turn_left':
                self.turn('left')
            case 'turn_right':
                self.turn('right')
    
    def turn(self, direction: str):
        self.leg_count = self.leg_count % 5
        poses_dict = self.turn_left_poses if direction == 'left' else self.turn_right_poses
        match self.leg_count:
            case 0:
                self.swingLegTo('rear_left', poses_dict['rear_left_start'])
            case 3:
                self.swingLegTo('front_left', poses_dict['front_left_start'])
            case 2:
                self.swingLegTo('rear_right', poses_dict['rear_right_start'])
            case 1:
                self.swingLegTo('front_right', poses_dict['front_right_start'])
            case 4:
                self.turnLegTo('rear_left', poses_dict['rear_left_end'], 'left')
                self.turnLegTo('front_left', poses_dict['front_left_end'], 'left')
                self.turnLegTo('rear_right', poses_dict['rear_right_end'], 'left')
                self.turnLegTo('front_right', poses_dict['front_right_end'], 'left')
        self.leg_count += 1

    def stop(self):
        self.leg_count = self.leg_count % 4
        match self.leg_count:
            case 0:
                self.swingLegTo('rear_left', Pose())
                self.leg_count += 1
            case 1:
                self.swingLegTo('front_left', Pose())
                self.leg_count += 1
            case 2:
                self.swingLegTo('rear_right', Pose())
                self.leg_count += 1
            case 3:
                self.swingLegTo('front_right', Pose())
                self.leg_count += 1

    def step_leg(self):
        if not self.is_initiated:
            return
        self.leg_count = self.leg_count % 6
        match self.leg_count:
            case 0:
                self.swingLegTo('rear_left', self.walking_poses['rear_left'])
                self.leg_count += 1
            case 1:
                self.swingLegTo('front_left', self.walking_poses['front_left'])
                self.leg_count += 1
            case 2:
                self.moveAllLegsBack(0.035)
                self.leg_count += 1
            case 3:
                self.swingLegTo('rear_right', self.walking_poses['rear_right'])
                self.leg_count += 1
            case 4:
                self.swingLegTo('front_right', self.walking_poses['front_right'])
                self.leg_count += 1
            case 5:
                self.moveAllLegsBack(0.035)
                self.leg_count += 1

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

    def turnLegTo(self, leg:str, pose:Pose, direction:str):
        state = LegState()
        state.is_swing = False
        if direction == 'left':
            state.turn_left = True
            state.turn_right = False
        if direction == 'right':
            state.turn_left = False
            state.turn_right = True
        state.pose = pose
        self.legs[leg][1].publish(state)

    def swingLegTo(self, leg:str, pose:Pose):
        state = LegState()
        state.is_swing = True
        state.turn_left = False
        state.turn_right = False
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
    
    def getTransform(self, source: str, target='base_link') -> TransformStamped:
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
    if len(sys.argv) > 1:
        state = sys.argv[1]  # For example, first argument
    node = Quadruped(state)
    rclpy.spin(node)

if __name__ == '__main__':
    main()