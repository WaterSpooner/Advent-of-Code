def calculateMove(direction,pipe,xPos,yPos):
    if pipe == "F" and direction == 0:
        return (xPos+1,yPos,1)
    elif pipe == "7" and direction == 0:
        return (xPos-1,yPos,3)
    elif pipe == "J" and direction == 1:
        return (xPos,yPos-1,0)
    elif pipe == "L" and direction == 3:
        return (xPos,yPos-1,0)
    elif pipe == "F"and direction == 3:
        return (xPos,yPos+1,2)
    elif pipe == "7" and direction == 1:
        return (xPos,yPos+1,2)
    elif pipe == "J" and direction == 2:
        return (xPos-1,yPos,3)
    elif pipe == "L" and direction == 2:
        return (xPos+1,yPos,1)
    elif direction == 0 and (pipe == "|" or pipe == "S"):
        return (xPos,yPos-1 ,direction)
    elif direction == 1 and (pipe == "-" or pipe == "S"):
        return (xPos+1,yPos,direction)
    elif direction == 2 and (pipe == "|" or pipe == "S"):
        return (xPos,yPos+1,direction)
    elif direction == 3 and (pipe == "-" or pipe == "S"):
        return (xPos-1,yPos,direction)
    return (0,0,-1)

def findPath(Startx,Starty,pipes):
    maxY = len(pipes)
    maxX = len(pipes[0])
    for direction in range(3):
        path = []
        x,y = Startx,Starty
        while True:
            path.append((x,y))
            pipe = pipes[y][x]
            x,y,direction = calculateMove(direction,pipe,x,y)
            if x < 0 or x >= maxX or y < 0 or y >= maxY or pipes[y][x] == "." or direction == -1:
                break
            if x == Startx and y == Starty:
                return path

def findStart(pipes):
    for y in range(len(pipes)):
        for x in range(len(pipes[y])):
            if pipes[y][x] == "S":
                return (x,y)
            

file = open("input.txt")
pipes = [list(line) for line in file.read().split("\n")]
startX,startY = findStart(pipes)
path = findPath(startX,startY,pipes)
print(len(path)//2)

