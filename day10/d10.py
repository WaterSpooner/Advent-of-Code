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
    return None


file = open("day10/input.txt")
pipes = [list(line) for line in file.read().split("\n")]
startXPos = 0
startYPos = 0
maxY = len(pipes)
maxX = len(pipes[0])
for y in range(len(pipes)):
    for x in range(len(pipes[y])):
        if pipes[y][x] == "S":
            startXPos = x
            startYPos = y
            break
mainLoop = []
for i in range(4):
    valid = True
    loop = []
    xPos,yPos = startXPos,startYPos
    direction = i
    loop.append((xPos,yPos))
    while True:
        if calculateMove(direction,pipes[yPos][xPos],xPos,yPos) == None:
            loop = []
            break    
        xPos,yPos,direction = calculateMove(direction,pipes[yPos][xPos],xPos,yPos)
        loop.append((xPos,yPos))
        if xPos < 0 or xPos >= maxX or yPos < 0 or yPos >= maxY:
            loop = []
            break
        if pipes[yPos][xPos] == ".":
            loop = []
            break
        if pipes[yPos][xPos] == "S":
            break
    if len(loop) > 0:
        mainLoop = loop
enclosed = 0
xOff = mainLoop[-2][0] - mainLoop[1][0]
yOff = mainLoop[-2][1] - mainLoop[1][1]
if xOff == 1 and yOff == -1:
    pipes[startYPos][startXPos] = "F"
elif xOff == -1 and yOff == 1:
    pipes[startYPos][startXPos] = "J"
elif xOff == 1 and yOff == 1:
    pipes[startYPos][startXPos] = "7"
elif xOff == -1 and yOff == -1:
    pipes[startYPos][startXPos] = "L"
elif xOff != 0:
    pipes[startYPos][startXPos] = "-"
elif yOff != 0:
    pipes[startYPos][startXPos] = "|"
pipes[startYPos][startXPos] = "J"
for y in range(maxY):
    print(y)
    for x in range(maxX):
        if (x,y) in mainLoop:
            continue
        count = 0
        horizontal = False
        for xRay in range(x):
            if ((xRay,y) in mainLoop):
                if pipes[y][xRay] == "7" or pipes[y][xRay] == "F" or pipes[y][xRay] == "|":
                    count +=1
        if count %2 == 1:
            enclosed += 1
print(enclosed)

#print(len(mainLoop)//2)
#print(mainLoop[0])
