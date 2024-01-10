import numpy as np

def compare(string1,string2):
    count = 0
    for a,b in zip(string1,string2):
        if a != b:
            if count == 1:
                return -1
            count += 1
    return count

def column(grid):
    grid = [np.array(list(line)) for line in grid]
    grid = np.array(grid)
    return ["".join(grid[:,i]) for i in range(len(grid[0]))]

def mirror(mirrorIndex,lines):
    total = 0
    startPointer = mirrorIndex
    endPointer = mirrorIndex +1
    while startPointer >= 0 and endPointer < len(lines):
        v = compare(lines[startPointer], lines[endPointer])
        if v == 0 or v == 1 and total == 0:
            total += v
            startPointer -= 1
            endPointer += 1
        else:
            return False
    return total != 0

def midpoint(vertical,horizontal):
    for x in range(len(vertical)-1):
        if mirror(x,vertical):
            return (x+1)*100   
    for x in range(len(horizontal)-1):
        if mirror(x,horizontal):
            return (x+1) 
    return 0

file = open("input.txt", "r")
input = [line.split("\n") for line in file.read().split("\n\n")]
total = 0
for grid in input:
    horizontal = grid
    vertical = column(grid)
    total += midpoint(horizontal,vertical)
print(total)