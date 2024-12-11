from math import dist
import heapq
from random import randint, seed
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from itertools import product
import rclpy
from rclpy.node import Node
import numpy as np
from random import randrange
from PIL import Image
from nav_msgs.msg import Path, OccupancyGrid
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped, PoseStamped, Pose
from rclpy import time

def genGrid(rows, cols, tarCov, maxFailCount=1000):
    grid = np.zeros([rows, cols])
    curCov = 0
    count = 0
    shapeI = np.array([[1,0],[1,0],[1,0],[1,0]])
    shapeL = np.array([[1,1],[0,1],[0,1],[0,0]])
    shapeZ = np.array([[1,0],[1,1],[0,1],[0,0]])
    shapeT = np.array([[0,1],[1,1],[0,1],[0,0]])
    shapes = np.array([shapeI, shapeL, shapeZ, shapeT])
    while curCov <= tarCov or count >= maxFailCount:
        randRow = randrange(rows)
        randCol = randrange(cols)
        randShapeID = randrange(np.size(shapes,0))
        randShape = shapes[randShapeID]
        randPos = (randRow, randCol)
        randRot = randrange(4)
        randShape = np.rot90(randShape, randRot)
        placedShape, grid = placeShape(grid, randShape, randPos)
        if not placedShape:
            count += 1
        curCov = np.sum(grid)/np.size(grid)
    return grid

def placeShape(grid, shape, pos):
    shape = shape[~np.all(shape == 0, axis=1)]
    shape = shape[:,~np.all(shape == 0, axis=0)]
    shapeRows = np.size(shape,0)
    shapeCols = np.size(shape,1)
    gridRows = np.size(grid,0)
    gridCols = np.size(grid,1)
    rowsCheck = pos[0] >= 0 and pos[0]+shapeRows <= gridRows
    colsCheck = pos[1] >= 0 and pos[1]+shapeCols <= gridCols
    if rowsCheck and colsCheck:
        gridSpace = grid[pos[0]:pos[0]+shapeRows,pos[1]:pos[1]+shapeCols]
        preNumFilled = np.size(np.nonzero(gridSpace))
        newSpace = gridSpace + shape
        numFilled = np.count_nonzero(newSpace)
        if numFilled - preNumFilled == np.sum(shape):
            grid[pos[0]:pos[0]+shapeRows,pos[1]:pos[1]+shapeCols] = newSpace
        return True, grid
    return False, grid

def genHeightmap(filePath, grid):
    newImage = Image.fromarray(grid)

    if newImage.mode != 'RGB':
        newImage = newImage.convert('RGB')

    newImage.save(filePath)


class AStar:
    def heuristic(a, b):
        return dist(a, b)

    def find_path(grid, start, goal, max_steps):
        rows, cols = grid.shape
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {start : None}
        g_score = {start: 0}
        h_score = {start : AStar.heuristic(start, goal)}
        f_score = {start: g_score[start] + h_score[start]}
        num_steps = 0

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for dx, dy in list(product([-1,0,1],[-1,0,1])):
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor] == 0:
                    tentative_g_score = g_score[current] + dist(current, neighbor)
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        h_score[neighbor] = AStar.heuristic(neighbor, goal)
                        f_score[neighbor] = g_score[neighbor] + h_score[neighbor]
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

            num_steps += 1
            if num_steps > max_steps:
                return None
        return None

class RRT(Node):
    def __init__(self, node_name, grid, max_dist, max_depth=1000):
        super().__init__(node_name)
        self.tf_broadcaster = StaticTransformBroadcaster(self)
        self.pathPublisher = self.create_publisher(Path, '/get_RRT_data', 1)
        self.gridPublisher = self.create_publisher(OccupancyGrid, '/get_grid_data', 1)
        self.grid = grid
        self.graph = {}
        self.max_dist = max_dist
        self.max_depth = max_depth
        com = TransformStamped()
        com.header.stamp = self.get_clock().now().to_msg()
        com.header.frame_id = 'map'
        com.child_frame_id = 'rrt_center'
        com.transform.translation.x = 0.0
        com.transform.translation.y = 0.0
        com.transform.translation.z = 0.0
        com.transform.rotation.x = 0.0
        com.transform.rotation.y = 0.0
        com.transform.rotation.z = 0.0
        com.transform.rotation.w = 1.0
        self.grid_msg = None
        self.path_msg = None
        self.timer = self.create_timer(0.1, self.publish_help)

        self.tf_broadcaster.sendTransform(com)

    def publish_help(self):
        if self.grid_msg is not None:
            self.gridPublisher.publish(self.grid_msg)
        if self.path_msg is not None:
            self.pathPublisher.publish(self.path_msg)


    def random_sample(self):
        rows, cols = self.grid.shape
        while True:
            sample = (randint(0, rows - 1), randint(0, cols - 1))
            if self.grid[sample] == 0 and sample not in self.graph:
                return sample

    def add_edge(self, start, goal, path):
        self.graph[start].append((goal, path))
        self.graph[goal].append((start, path[::-1]))

    def build_rrt(self, num_samples):
        nodes = []
        for _ in range(num_samples):
            sample = self.random_sample()
            nodes.append(sample)
        for node in nodes:
            self.add_node(node)

    def add_node(self, new_node):
        if new_node not in self.graph:
            self.graph[new_node] = []
            
            for existing_node in list(self.graph.keys()):
                if existing_node != new_node:
                    path = AStar.find_path(self.grid, existing_node, new_node, self.max_depth)
                    if path and len(path) <= self.max_dist:
                        self.add_edge(existing_node, new_node, path)

    def save_graph(self, filename):
        graph_dict = {str(key): [(str(neighbor), path) for neighbor, path in value] for key, value in self.graph.items()}
        with open(filename, 'w') as f:
            json.dump(graph_dict, f, indent=4)

    def load_graph(self, filename):
        with open(filename, 'r') as f:
            graph_dict = json.load(f)
        self.graph = {eval(key): [(eval(neighbor), path) for neighbor, path in value] for key, value in graph_dict.items()}

    def find_path(self, start, goal):
        update_graph = start not in self.graph or goal not in self.graph
        self.add_node(start)
        self.add_node(goal)
        if update_graph:
            self.save_graph('src/robot_sim/worlds/rrt_graph.json')
            self.load_graph('src/robot_sim/worlds/rrt_graph.json')

        visited = set()
        queue = [(start, [])]
        while queue:
            current, path = queue.pop(0)
            if current == goal:
                return path
            visited.add(current)
            for neighbor, segment in self.graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + segment))
        return None
    
    def gen_path_msg(self, path):
        msg = Path()
        pathList = [PoseStamped()] * len(path)
        for index, q in enumerate(path):
            ps = PoseStamped()
            ps.pose.position.y = (q[0]*1.0 - 15)
            ps.pose.position.x = (q[1]*1.0 - 15)
            ps.header.frame_id = 'rrt_center'
            ps.header.stamp = time.Time().to_msg()
            pathList[index] = ps
        msg.poses = pathList
        msg.header.frame_id = 'rrt_center'
        msg.header.stamp = time.Time().to_msg()
        # self.get_logger().info(f"{pathList}")
        return msg
    
    def gen_grid_msg(self, grid):
        msg = OccupancyGrid()
        msg.info.height = len(grid)
        msg.info.width = len(grid[0])
        msg.info.resolution = 1.0
        ogn = Pose()
        ogn.position.x = -16.0
        ogn.position.y = -16.0
        msg.info.origin = ogn
        msg.data = np.reshape(grid*100, [len(grid)*len(grid[0])]).astype(int)
        msg.header.frame_id = 'rrt_center'
        msg.header.stamp = time.Time().to_msg()
        return msg

    def plot_graph(self, display=True, filepath=None):
        plt.figure(figsize=(10, 10))
        plt.imshow(self.grid, cmap='gray_r')

        for _, edges in self.graph.items():
            for _, path in edges:
                path_x, path_y = zip(*path)
                plt.plot(path_y, path_x, color='blue', linewidth=0.5)

        nodes_x, nodes_y = zip(*self.graph.keys())
        plt.scatter(nodes_y, nodes_x, color='red', s=10, zorder=5)

        legend_elements = [
            Patch(facecolor='black', edgecolor='black', label='Obstacles'),
            plt.Line2D([0], [0], color='blue', linewidth=1, label='Paths'),
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=5, label='Nodes')
        ]

        plt.title('RRT Graph')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend(handles=legend_elements)

        if filepath != None:
            plt.savefig(filepath)

        plt.show()
        

def main(args=None):
    filePathHM = "src/robot_sim/worlds/Heightmap.png"
    filePathRRT = "src/robot_sim/worlds/rrt_graph.json"
    filePathPlt = "src/robot_sim/worlds/RRT_Graph.png"

    rows = 32
    cols = 32
    tarCov = 0.1
    maxDist = 10
    numSamples = 50
    showFig = True

    start_Q = (15, 15)
    goal_Q = (16,24)
    seed(1234)
    grid = genGrid(rows, cols, tarCov)
    genHeightmap(filePathHM, grid)

    rclpy.init(args=args)

    node = RRT('rrt', grid, maxDist)

    node.build_rrt(numSamples)
    node.save_graph(filePathRRT)
    node.load_graph(filePathRRT)

    path = node.find_path(start_Q, goal_Q)

    node.path_msg = node.gen_path_msg(path)

    node.plot_graph(showFig, filePathPlt)

    node.grid_msg = node.gen_grid_msg(grid)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()
