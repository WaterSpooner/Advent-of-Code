file = open("input.txt", "r")
values = [[int(number) for number in line.split(" ")] for line in file.read().split("\n")]
totalCount = 0
for value in values:
    difference = value
    count = 0
    i = 0
    while difference.count(0) != len(difference):
        oldDifference = difference.copy()
        count += difference[0] if i % 2 == 0 else  difference[0]*-1
        difference = []
        for i in range(len(oldDifference)-1):
            difference.append(oldDifference[i+1]-oldDifference[i])
    totalCount += count
print(totalCount)