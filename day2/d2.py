import re

f = open("day2//input.txt", "r")
text = f.read()
lines = text.split('\n')
count = 0
for i,line in enumerate(lines):
    line = line[line.find(':')+2:]
    games = line.split(';')
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for game in games:
        green = sum([int(x) for x in re.findall('(\d+)(?: green)',game)])
        red = sum([int(x) for x in re.findall('(\d+)(?: red)',game)])
        blue = sum([int(x) for x in re.findall('(\d+)(?: blue)',game)])
        if green > maxGreen:
            maxGreen = green
        if red > maxRed:
           maxRed = red
        if blue > maxBlue:
            maxBlue = blue
    count += maxBlue*maxGreen*maxRed
print(count)