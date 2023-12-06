import re
import math
file = open("day6/input.txt", "r")
text = file.read()
data = []
for line in text.split('\n'):
    line = re.split('\s+', line )
    line.pop(0)
    line = "".join(line)
    data.append([int(line)])
count = 1
for i in range(len(data[0])):
    time = data[0][i]
    distance = data[1][i]
    root = time**2 - 4*distance
    sqrt = root**0.5
    lb = math.ceil((time - sqrt+0.0001)/2)
    up = math.floor((time + sqrt-0.0001)/2)
    count *= (up-lb+1)
print(count)