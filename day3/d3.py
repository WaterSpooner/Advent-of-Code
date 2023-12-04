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
    return -1

def validGear(match,width,height,noNumbers,dict):
    number = int(match.group())
    startIndex = (match.start()%width,match.start()//width)
    endIndex = ((match.end()-1)%width,(match.end()-1)//width)
    for y in range(startIndex[1]-1,endIndex[1]+2):
        for x in range(startIndex[0]-1,endIndex[0]+2):
            if 0 <= x < width and 0 <= y < height:
                if noNumbers[y][x] == '*':
                    numbers = dict.get((x,y),[])
                    numbers.append(number)
                    dict[(x,y)] = numbers
                    return dict
    return dict

f = open("day3//input.txt", "r")
text = f.read()
copyText = text
lines = text.split('\n')
width = len(lines[0])
height = len(lines)
line = "w".join(lines)
noNumbers = re.sub('[0-9]', '.', line)
noNumbers = noNumbers.split('w')
line = re.sub('w', '', line)
dict = {}
for match in re.finditer('\d{1,3}', line):
    dict = validGear(match,width,height,noNumbers,dict)
sum = 0
for star in dict:
    if len(dict[star]) ==2:
        sum += dict[star][0]*dict[star][1]
print(sum)

