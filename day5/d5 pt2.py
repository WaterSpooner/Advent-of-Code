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
newNumbers = []
for n in range(0,len(numbers[0][0]),2):
    print(n)
    nums = list(range(numbers[0][0][n],numbers[0][0][n]+numbers[0][0][n+1]))
    newNumbers += nums
print("done")
for i,seed in enumerate(newNumbers):
    print(i/len(newNumbers))
    destination = seed
    for i in range(1, len(numbers)):
        for num in numbers[i]:
            if num[1] <= destination < (num[1]+num[2]):
                destination = destination - num[1] + num[0]
                break
    lowestDesintaion = destination if destination < lowestDesintaion else lowestDesintaion
print(lowestDesintaion)
