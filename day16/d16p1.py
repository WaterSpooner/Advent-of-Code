import numpy as np

def move(pos):
    if pos[2] == 0:
        return pos[0],pos[1]-1,pos[2]
    elif pos[2] == 1:
        return pos[0]+1,pos[1],pos[2]
    elif pos[2] == 2:
        return pos[0],pos[1]+1,pos[2]
    elif pos[2] == 3:
        return pos[0]-1,pos[1],pos[2]

def nextPos(char,pos):
    mirror = {0:1,1:0,2:3,3:2}
    if char == "." or (char == "-" and pos[2] % 2 == 1) or (char == "|" and pos[2] % 2 == 0):
        return [move(pos)]
    elif char == "\\": 
        return [move((pos[0],pos[1],3-pos[2]))]
    elif char == "/":
        return [move((pos[0],pos[1],mirror[pos[2]]))]
    elif char == "-" and pos[2] % 2 == 0: 
        return [move((pos[0],pos[1],1)),move((pos[0],pos[1],3))]
    elif char == "|" and pos[2] % 2 == 1:
        return [move((pos[0],pos[1],0)),move((pos[0],pos[1],2))]

def path(tiles,spaces,grid,pos):
    char = grid[pos[1]][pos[0]]
    queue = nextPos(char,pos)
    while len(queue) > 0:
        m = queue.pop(0)
        if m[0] < 0 or m[1] < 0 or m[0] >= grid.shape[1] or m[1] >= grid.shape[0]:
            continue
        if m in spaces:
            continue
        spaces[m] = 1
        tiles[(m[0],m[1])] = 1
        queue.extend(nextPos(grid[m[1]][m[0]],m))
    return
    
text = open("input.txt").read().split("\n")
grid = np.array([list(line) for line in text])
spaces = {}
tiles = {}
tiles[(0,0)] = 1
spaces[(0,0,1)] = 1
path(tiles,spaces,grid,(0,0,1))
print(sum(tiles.values()))