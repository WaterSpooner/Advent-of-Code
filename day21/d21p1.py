def findStart(grid):
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c == "S":
                return x,y
def inRange(height,width,x,y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return False
    return True

def move(position,grid):
    moves = set()
    height = len(grid)
    width = len(grid[0])
    x,y = position
    if inRange(height,width,x+1,y) and grid[y][x+1] != "#":
        moves.add((x+1,y))
    if inRange(height,width,x-1,y) and grid[y][x-1] != "#":
        moves.add((x-1,y))
    if inRange(height,width,x,y+1) and grid[y+1][x] != "#":
        moves.add((x,y+1))   
    if inRange(height,width,x,y-1) and grid[y-1][x] != "#":
        moves.add((x,y-1))
    return moves
              

grid = [list(line) for line in open("input.txt", "r").read().split("\n")]
startX,startY = findStart(grid)
exploredCount = 0
newQueue = {(startX,startY)}
for i in range(64):
    exploredCount = 0
    queue = newQueue.copy()
    newQueue = set()
    while len(queue) > 0:
        position = queue.pop()
        newQueue.update(move(position,grid))
    exploredCount = len(newQueue) 
print(exploredCount) 

