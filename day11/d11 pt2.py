import numpy as np
file = open("day11/input.txt",'r')
grid = np.array([list(line) for line in file.read().split("\n")])
height, width = grid.shape
coords = np.where(grid=='#')
xVals = np.unique(coords[0])
yVals = np.unique(coords[1])
locations = []
rowExpansion = []
columnExpansion = []
for i in range(len(coords[0])):
    locations.append((coords[0][i],coords[1][i]))
for x in range(width):
    if np.count_nonzero(grid[:,x] == '#') == 0:
        columnExpansion.append(1000000)
    else:
        columnExpansion.append(1)
for y in range(height):
    if np.count_nonzero(grid[y,:] == '#') == 0:
        rowExpansion.append(1000000)
    else:
        rowExpansion.append(1)
rowExpansion = np.array(rowExpansion)
columnExpansion = np.array(columnExpansion)
count = 0
for i in range(len(locations)):
    for j in range(i+1,len(locations)):
        count += (np.sum(rowExpansion[np.arange(x1,x2)],))
        count += (np.sum(columnExpansion[np.arange(y1 ,y2)],dtype=np.int64))
print(count)