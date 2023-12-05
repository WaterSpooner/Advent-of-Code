import re
file = open('input.txt', 'r')
text =file.read()
lines = text.split('\n')
count = 0
for line in lines:
    line = re.sub('^.*?:', '', line)
    line = re.sub(' +', ' ', line)
    winners = [int(x) for x in line.split('|')[0].strip().split(' ')]
    numbers = [int(x) for x in line.split('|')[1].strip().split(' ')]
    score = len(set(winners)&set(numbers))
    count += pow(2, score-1) if score > 0 else 0    
print(count)
