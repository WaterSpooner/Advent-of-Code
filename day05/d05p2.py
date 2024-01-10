import re
file = open("input.txt", "r")
text = file.read()
text = re.split(r'[a-z\-\:]+', text)
numbers = []
for line in text:
    if line.strip() == '':
        continue
    line = re.split(r'\n', line.strip())
    numbers.append([[int(i) for i in x.split(' ')] for x in line])

seeds = numbers.pop(0)[0]
source =[]
destination = []
for i in range(0,len(seeds),2):
    destination.append((seeds[i], seeds[i]+seeds[i+1]-1))

for numList in numbers:
    source = destination
    destination = []
    seedList= source.copy()
    for seed in source:
         for num in numList:
            if num[1] <= seed[0] < (num[1]+num[2]):
                if num[1] <= seed[1] < (num[1]+num[2]):
                        destination.append((seed[0] - num[1] + num[0],seed[1] - num[1] + num[0]))
                        seedList.remove(seed)
                else:
                    seedList.remove(seed)
                    destination.append((seed[0] - num[1] + num[0],num[0]+num[2]-1)) 
                    source.append((num[1]+num[2],seed[1]))
                    seedList.append((num[1]+num[2],seed[1]))
    for seed in seedList:
        destination.append(seed)

lowest = destination[0][0]
for v in destination:
    if v[0] < lowest:
        lowest = v[0]
print(lowest)
