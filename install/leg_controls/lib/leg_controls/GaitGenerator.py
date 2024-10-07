#/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Pose

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

import numpy as np
import time
import asyncio
import threading

INITIAL_POSE = np.array([-30, -120, 0])

class WalkingGait(Node):
    def __init__(self, pub_topic):
        super().__init__('walking_gait')
        self.fl_publisher = self.create_publisher(Pose, '/front_left_ee_pose', 10)
        self.fr_publisher = self.create_publisher(Pose, '/front_right_ee_pose', 10)
        self.rl_publisher = self.create_publisher(Pose, '/rear_left_ee_pose', 10)
        self.rr_publisher = self.create_publisher(Pose, '/rear_right_ee_pose', 10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.publisher = self.create_publisher(Pose, pub_topic, 10)

        self.fl_pose = INITIAL_POSE
        self.fr_pose = INITIAL_POSE
        self.rl_pose = INITIAL_POSE
        self.rr_pose = INITIAL_POSE

        thread = threading.Thread(target=rclpy.spin, args=(self, ), daemon=True)
        thread.start()
        self.rate = self.create_rate(20)
    
    def generateSwing(self, start, end, height):
        P0 = start
        P3 = end
        P1 = np.array([P0[0], P0[1]+height, P0[2]])
        P2 = np.array([P3[0], P3[1]+height, P3[2]])
        steps = np.linspace(0, 1, 20)
        B = np.zeros((3, 20))
        idx = 0
        for step in steps:
            B[:, idx] = (1-step)**3*P0 + 3*(1-step)**2*step*P1 + 3*(1-step)*step**2*P2 + step**3*P3
            idx += 1
        return B

    def generateStance(self, start, end, seconds):
        P0 = start
        P1 = end
        steps = np.linspace(0, 1, 20*seconds)
        B = np.zeros((3, 20*seconds))
        idx = 0
        for step in steps:
            B[:, idx] = (1-step)*P0 + step*P1
            idx += 1
        return B

    def moveThroughTrajectory(self, trajectory):
        ## Ideally, trajectory is a 12x80 array.
        for column in range(trajectory.shape[1]):
            fl_traj = trajectory[0:3, column]  # First two rows for FL
            fr_traj = trajectory[3:6, column]  # Next two rows for FR
            rl_traj = trajectory[6:9, column]  # Next two rows for RL
            rr_traj = trajectory[9:12, column]  # Next two rows for RR

            # Front Left
            fl_pose = Pose()
            fl_pose.position.x = fl_traj[0]
            fl_pose.position.y = fl_traj[1]
            fl_pose.position.z = fl_traj[2]
        
            fr_pose = Pose()
            fr_pose.position.x = fr_traj[0]
            fr_pose.position.y = fr_traj[1]
            fr_pose.position.z = fr_traj[2]

            rl_pose = Pose()
            rl_pose.position.x = rl_traj[0]
            rl_pose.position.y = rl_traj[1]
            rl_pose.position.z = rl_traj[2]

            rr_pose = Pose()
            rr_pose.position.x = rr_traj[0]
            rr_pose.position.y = rr_traj[1]
            rr_pose.position.z = rr_traj[2]

            self.fl_publisher.publish(fl_pose)
            self.fr_publisher.publish(fr_pose)
            self.rl_publisher.publish(rl_pose)
            self.rr_publisher.publish(rr_pose)

            self.rate.sleep()

    def generateTrajectory(self, poses):
        ## Returns a 12x80 matrix. every 3 rows is one leg. 80 steps
        new_fl_pose = poses[0]
        new_fr_pose = poses[1]
        new_rl_pose = poses[2]
        new_rr_pose = poses[3]

        ## Generate all the trajectories

        height = 80

        fl_swing = self.generateSwing(self.fl_pose, new_fl_pose, height)
        fl_stance = self.generateStance(new_fl_pose, self.fl_pose, 3)

        fr_swing = self.generateSwing(self.fr_pose, new_fr_pose, height)
        fr_stance = self.generateStance(new_fr_pose, self.fr_pose, 3)

        rl_swing = self.generateSwing(self.rl_pose, new_rl_pose, height)
        rl_stance = self.generateStance(new_rl_pose, self.rl_pose, 3)

        rr_swing = self.generateSwing(self.rr_pose, new_rr_pose, height)
        rr_stance = self.generateStance(new_rr_pose, self.rr_pose, 3)

        # Surgery to make them connect nicely (SO UNBELIEVABLY TEMPORARY)
        # Swing Order: fl -> fr -> rl -> rr -> repeat

        fl_trajectory = np.concatenate((fl_swing,fl_stance),axis=1)  # swing, stance
        fr_trajectory = np.concatenate((fr_stance[:, -20:],fr_swing, fr_stance[:, :40]),axis=1)  # 1/3 stance, swing, 2/3 stance
        rl_trajectory = np.concatenate((rl_stance[:, -40:],rl_swing, rl_stance[:, :20]),axis=1)  # 2/3 stance, swing, 1/3 stance
        rr_trajectory = np.concatenate((rr_stance,rr_swing),axis=1)  # stance, swing

        ## Concatenate all trajectories to return. This should make a 12x80 array
        return np.concatenate(
            (fl_trajectory, fr_trajectory, rl_trajectory, rr_trajectory),
            axis=0
        )

    def getTransform(self, target: str, source: str):
        try:
            future_transform = self.tf_buffer.wait_for_transform_async(
                target,
                source,
                rclpy.time.Time(),
            )

            rclpy.spin_until_future_complete(self, future_transform)

            transform = asyncio.run(self.tf_buffer.lookup_transform_async(
                target,
                source,
                rclpy.time.Time(),
            ))
            return transform
        except Exception as e:
            self.get_logger().error(f"Could not lookup transform: {e}")
            return None


def main(args=None):
    rclpy.init(args=args)
    walk = WalkingGait('/front_left_ee_pose')
    poses = [
        np.array([-30, -120, 0 + 30]),
        np.array([-30, -120, 0 + 30]),
        np.array([-30, -120, 0 + 30]),
        np.array([-30, -120, 0 + 30])
    ]
    traj = walk.generateTrajectory(poses)
    while True:
        walk.moveThroughTrajectory(traj)
            

if __name__=='__main__':
    main()