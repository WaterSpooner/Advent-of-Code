import re
def validNum(match,width,height,noNumbers):
    number = int(match.group())
    startIndex = (match.start()%width,match.start()//width)
    endIndex = ((match.end()-1)%width,(match.end()-1)//width)
    for y in range(startIndex[1]-1,endIndex[1]+2):
        for x in range(startIndex[0]-1,endIndex[0]+2):
            if 0 <= x < width and 0 <= y < height:
                if noNumbers[y][x] != '.':
                    return number
    return 0

f = open("input.txt", "r")
text = f.read()
copyText = text
lines = text.split('\n')
width = len(lines[0])
height = len(lines)
line = "w".join(lines)
noNumbers = re.sub(r'[0-9]', '.', line)
noNumbers = noNumbers.split('w')
line = re.sub(r'w', '', line)
dict = {}
count = 0
for match in re.finditer(r'\d{1,3}', line):
    count += validNum(match,width,height,noNumbers)
print(count)

