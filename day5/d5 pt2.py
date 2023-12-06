import re
file = open("day5/input.txt", "r")
text = file.read()
text = re.split('[a-z\-\:]+', text)
numbers = []
for line in text:
    if line.strip() == '':
        continue
    line = re.split('\n', line.strip())
    numbers.append([[int(i) for i in x.split(' ')] for x in line])

seeds = numbers.pop(0)[0]
oldDestination = {}
seedRange =[]

for i in range(0,len(seeds),2):
    oldDestination[(seeds[i], seeds[i]+seeds[i+1]-1)] = (seeds[i], seeds[i]+seeds[i+1]-1)

for numList in numbers:
    destination = dict.fromkeys(oldDestination.values(),9999999999999999999)
    seedRange = list(destination.keys())
    for seed in seedRange:
         for num in numList:
            if num[1] <= seed[0] < (num[1]+num[2]):
                if num[1] <= seed[1] < (num[1]+num[2]):
                        destination[seed] = (seed[0] - num[1] + num[0],seed[1] - num[1] + num[0]) if destination[seed][0] > (seed[0] - num[1] + num[0]) else destination[seed]
                else:
                    if destination[seed] != 9999999999999999999:
                        destination[seed] = -2
                    destination[(seed[0],num[1]+num[2]-1)] = (seed[0] - num[1] + num[0],seed[1] - num[1] + num[0]-1) 
                    destination[(num[1]+num[2],seed[1])] = 9999999999999999999
                    seedRange.append((num[1]+num[2],seed[1]))
    for dest in destination.keys():
        if destination[dest] == 9999999999999999999:
            destination[dest] = dest
    destination = {k:v for k,v in destination.items() if v != -2}
    oldDestination = destination



values = list(destination.values())
print(values)
lowest = values[0][0]
for v in values:
    if v[0] < lowest:
        lowest = v[0]
print(lowest)
