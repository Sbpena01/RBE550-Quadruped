from PIL import Image
from gen_array import genGrid
from random import seed

path = "Heightmap.png"
# Open the image
image = Image.open(path)

rows, cols = image.size

tarCov = 0.1
maxFailCount = 1000
seed(0)

grid = genGrid(rows, cols, tarCov, maxFailCount) * 1
newImage = Image.fromarray(grid)

if newImage.mode != 'RGB':
    newImage = newImage.convert('RGB')

newImage.save(path)
