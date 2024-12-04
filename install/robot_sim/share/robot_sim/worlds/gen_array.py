import numpy as np
from random import randrange, seed

def genGrid(rows, cols, tarCov, maxFailCount):
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
