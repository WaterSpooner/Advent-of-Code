import re

f = open("input.txt", "r")
lines = f.readlines()
count = 0
for i,line in enumerate(lines):
    line = line[line.find(':')+2:]
    games = line.split(';')
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for game in games:
        green = sum([int(x) for x in re.findall(r'(\d+)(?: green)', game)])
        red = sum([int(x) for x in re.findall(r'(\d+)(?: red)', game)])
        blue = sum([int(x) for x in re.findall(r'(\d+)(?: blue)', game)])
        if green > maxGreen:
            maxGreen = green
        if red > maxRed:
           maxRed = red
        if blue > maxBlue:
            maxBlue = blue
    count += maxBlue*maxGreen*maxRed
print(count)