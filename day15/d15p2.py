def value(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

text = open("input.txt").read().split(",")
boxes = {}
for line in text:
    subString = ""
    lens = ""
    if line[-1] == '-':
        subString = line[:-1]
        lenses = boxes.get(value(subString),{})
        lenses.pop(subString,None)
        boxes[value(subString)] = lenses
    else:
        subString,lens = line.split("=")
        lenses = boxes.get(value(subString),{})
        lenses[subString] = lens
        boxes[value(subString)] = lenses
total = 0
for boxKey,boxValue in boxes.items():
    for i,lens in enumerate(boxValue.values()):
        total += (i+1)*int(lens) * (int(boxKey)+1)
print(total)