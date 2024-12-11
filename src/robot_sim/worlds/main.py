from gen_array import genGrid, genHeightmap
from RRT import RRT

filePathHM = "Heightmap.png"
filePathRRT = "rrt_graph.json"
filePathPlt = "RRT_Graph.png"

rows = 100
cols = 100
tarCov = 0.1
maxDist = 15
numSamples = 100
showFig = True

start_Q = (0, 0)
goal_Q = (49,49)

grid = genGrid(rows, cols, tarCov)
genHeightmap(filePathHM, grid)

rrt = RRT(grid, maxDist)
rrt.build_rrt(numSamples)
rrt.save_graph(filePathRRT)
rrt.load_graph(filePathRRT)

path = rrt.find_path(start_Q, goal_Q)

rrt.plot_graph(showFig, filePathPlt)
