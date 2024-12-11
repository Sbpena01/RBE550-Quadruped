from math import dist
import heapq
from random import randint
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from itertools import product

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

class RRT:
    def __init__(self, grid, max_dist, max_depth=1000):
        self.grid = grid
        self.graph = {}
        self.max_dist = max_dist
        self.max_depth = max_depth

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
            self.save_graph('rrt_graph.json')
            self.load_graph('rrt_graph.json')

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
        
