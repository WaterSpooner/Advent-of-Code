import numpy as np

def moveNorth(grid):
    newgrid = []
    for i in range(len(grid[0])):
        stack = []
        gaps = 0
        for j in range(len(grid)):
            if grid[j][i] == ".":
                gaps += 1
            if grid[j][i] == "O":
                stack.append("O")
            if grid[j][i] == "#":
                stack.extend(["."]*gaps)
                stack.append("#")
                gaps = 0
        stack.extend(["."]*gaps)
        newgrid.append(stack)
    newgrid = np.rot90(np.fliplr(np.array(newgrid)))
    return newgrid

def value(grid):
    total = 0
    height = len(grid)
    for i, row in enumerate(grid):
        total += np.count_nonzero(row=="O")*(height-i)
    return total
            
def stringify(grid):        
    return "\n".join(["".join(row) for row in grid])

text = open("input.txt").read().split("\n")
grid = [np.array(list(line)) for line in text]
grid = np.array(grid)
grid = moveNorth(grid)
print(value(grid))