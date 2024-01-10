import re
file = open('input.txt', 'r')
text =file.read()
lines = text.split('\n')
scores = []
counts = {}
for i,line in enumerate(lines):
    line = re.sub(r'^.*?:', '', line)
    line = re.sub(r' +', ' ', line)
    winners = [int(x) for x in line.split('|')[0].strip().split(' ')]
    numbers = [int(x) for x in line.split('|')[1].strip().split(' ')]
    score = len(set(winners)&set(numbers))
    scores.append(score)
    counts[i] = counts.get(i,0) + 1
    for x in range(i+1,i+score+1):
        counts[x] = counts.get(x,0) + counts[i]
print(sum(counts.values()))
