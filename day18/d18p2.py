def dig(instructions):
    position = (0,0)
    corners = [(0,0)]
    distance = 0
    for direction,length in instructions:
        length = int(length)
        if direction == "R":
            position = (position[0]+length,position[1])
        elif direction == "L":
            position = (position[0]-length,position[1])
        elif direction == "U":
            position = (position[0],position[1]-length)
        elif direction == "D":
            position = (position[0],position[1]+length)
        distance += length
        corners.append(position)
    return distance,corners

def area(corners):
    total = 0
    for i in range(len(corners)-1):
        total += corners[i][0]*corners[i+1][1]-corners[i+1][0]*corners[i][1]
    return abs(total/2)

def decode(hex):
    hex = hex[2:]
    distance = int(hex[0:-2],16)
    if hex[-2] == "0":
        return "R",distance
    elif hex[-2] == "1":
        return "D",distance
    elif hex[-2] == "2":
        return "L",distance
    elif hex[-2] == "3":
        return "U",distance

text = open("input.txt").read().split("\n")
instructions = [decode(text.split(" ")[2]) for text in text]
distance,corners = dig(instructions)
print(area(corners)+distance/2+1)