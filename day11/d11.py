import numpy as np
file = open("day11/input.txt",'r')
grid = np.array([list(line) for line in file.read().split("\n")])
height, width = grid.shape
xOff = 0
yOff = 0
newgrid = np.copy(grid)
for x in range(width):
    if np.count_nonzero(grid[:,x] == '#') == 0:
        newgrid = np.insert(newgrid,x+xOff, ".", axis=1)
        xOff += 1
for y in range(height):
    if np.count_nonzero(grid[y,:] == '#') == 0:
        newgrid = np.insert(newgrid,y+yOff, ".", axis=0)
        yOff += 1
coords = np.where(newgrid=='#')
locations = []
for i in range(len(coords[0])):
    locations.append((coords[0][i],coords[1][i]))
count  = 0
for i in range(len(locations)):
    for j in range(i+1,len(locations)):
        count += abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
print(count)