import re
file = open("day5/input.txt", "r")
text = file.read()
text = re.split('[a-z\-\:]+', text)
numbers = []
lowestDesintaion = 99999999999999999999
for line in text:
    if line.strip() == '':
        continue
    line = re.split('\n', line.strip())
    numbers.append([[int(i) for i in x.split(' ')] for x in line])
for x in range(0,len(numbers[0][0]),2):
    destination = numbers[0][0][x] + numbers[0][0][x+1]-1
    for i in range(1, len(numbers)):
        for num in numbers[i]:
            if num[1] <= destination < (num[1]+num[2]):
                destination = destination - num[1] + num[0]
                break
    lowestDesintaion = destination if destination < lowestDesintaion else lowestDesintaion
print(lowestDesintaion)
