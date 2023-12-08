import re
file = open("day8/input.txt", "r")
text = file.read()
text = re.sub("\(|\)| ","",text)
lines = text.split("\n")
instructions = list(lines.pop(0))
lines.pop(0)
graph = {}
node = "AAA"
endNode = "ZZZ"
for line in lines:
    line = line.split("=")
    graph[line[0]] = line[1].split(",")
i = 0
while node != "endNode":
    instruction = instructions[i%len(instructions)]
    i +=1
    if instruction == 'R':
        node = graph[node][1]
    else:
        node = graph[node][0]
print(i)