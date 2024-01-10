def dig(instructions):
    position = (0,0)
    corners = [(0,0)]
    distance = 0
    for direction,length,_ in instructions:
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

text = open("input.txt").read().split("\n")
instructions = [text.split(" ") for text in text]
distance,corners = dig(instructions)
print(area(corners)+distance/2+1)