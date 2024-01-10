def moveVertical(rocks,width,height,direction):
    rocks = rocks[::direction]
    rockStrings = []
    for i in range(width):
        rockString = ""
        gaps = 0
        for j in range(i,height*width,width):
            if rocks[j] == ".":
                gaps +=1
            if rocks[j] == "O":
                rockString += "O"
            if rocks[j] == "#":
                rockString += "."*gaps + "#"
                gaps = 0
        rockString += "."*gaps
        rockStrings.append(rockString)
    return ''.join(''.join(chars) for chars in zip(*rockStrings))[::direction]

def moveHorizontal(rocks,width,height,direction):
    rocks = rocks[::direction]
    rockString = ""
    for i in range(0,height*width,height):
        gaps = 0
        for j in range(i,i+width):
            if rocks[j] == ".":
                gaps +=1
            if rocks[j] == "O":
                rockString += "O"
            if rocks[j] == "#":
                rockString += "."*gaps + "#"
                gaps = 0
        rockString += "."*gaps
    return rockString[::direction]

def value(height,width,rockString):
    total = 0
    for i,char in enumerate(rockString):
        if char == "O":
            total += (height-(i//width))
    return total

text = open("input.txt").read().split("\n")
height,width = len(text),len(text[0])
rockString = "".join(text)
previous = {}
loopStart =-1
loopLen = -1
cycles = 1000000000
for cycle in range(cycles):
    rockString = moveVertical(rockString,height,width,1)
    rockString = moveHorizontal(rockString,height,width,1)
    rockString = moveVertical(rockString,height,width,-1)
    rockString = moveHorizontal(rockString,height,width,-1)
    if previous.get(rockString, -1) != -1:
        loopLen = cycle - previous[rockString][0]
        loopStart = previous[rockString][0]
        break
    previous[rockString] = cycle,rockString

offset = (cycles - loopStart)%loopLen
for k,v in previous.items():
    if v[0] == offset+loopStart-1:
        print(value(height,width,v[1]))
        break
