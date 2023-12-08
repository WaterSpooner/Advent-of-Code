import re
from collections import Counter
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


file = open("day8/input.txt", "r")
text = file.read()
text = re.sub("\(|\)| ","",text)
lines = text.split("\n")
instructions = list(lines.pop(0))
lines.pop(0)
graph = {}
startNodes = []
for line in lines:
    line = line.split("=")
    graph[line[0]] = line[1].split(",")
    if line[0][2] == 'A':
        startNodes.append(line[0])
nodelengths = []
for node in startNodes:
    i = 0
    while node[2] != 'Z':
        instruction = instructions[i%len(instructions)]
        if instruction == 'R':
            node = graph[node][1]
        else:
            node = graph[node][0]
        i +=1
    nodelengths.append(i)
lcm = {}
for length in nodelengths:
    lengthFactors = Counter(prime_factors(length))
    for l in lengthFactors:
        if l not in lcm or lengthFactors[l] > lcm[l]:
            lcm[l] = lengthFactors[l]
output = 1
for factor in lcm:
    output *= factor ** lcm[factor]
print(output) 