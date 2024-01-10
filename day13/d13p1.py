import numpy as np
def column(grid):
    grid = [np.array(list(line)) for line in grid]
    grid = np.array(grid)
    return ["".join(grid[:,i]) for i in range(len(grid[0]))]

def mirror(mirrorIndex,lines):
    startPointer = mirrorIndex
    endPointer = mirrorIndex +1
    while startPointer >= 0 and endPointer < len(lines):
        if lines[startPointer] == lines[endPointer]:
            startPointer -= 1
            endPointer += 1
        else:
            return False
    return True

def midpoint(lines):
    for x in range(len(lines)-1):
        if mirror(x,lines):
            return x
    return -1

file = open("input.txt", "r")
input = [line.split("\n") for line in file.read().split("\n\n")]
total = 0
for grid in input:
    horizontal = grid
    vertical = column(grid)
    total += (midpoint(horizontal)+1)*100 + midpoint(vertical)+1
print(total)