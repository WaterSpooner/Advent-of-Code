import re

f = open("input.txt", "r")
lines = f.readlines()
count = 0
for i,line in enumerate(lines):
    line = line[line.find(':')+2:]
    games = line.split(';')
    valid = True
    for game in games:
        green = sum([int(x) for x in re.findall(r'(\d+)(?: green)', game)])
        red = sum([int(x) for x in re.findall(r'(\d+)(?: red)', game)])
        blue = sum([int(x) for x in re.findall(r'(\d+)(?: blue)', game)])
        if (green > 13 or red > 12 or blue > 14):
            valid = False
    count += i + 1 if valid else 0
print(count)