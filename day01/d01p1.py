import re
f = open("input.txt", "r")
lines = f.readlines()
count = 0
nums = []
for line in lines:
    numString = re.findall(r'[1-9]',line)
    num = numString[0] + numString[-1]
    count += (int(num))
print(count)
