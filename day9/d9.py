file = open("day9/input.txt", "r")
values = [[int(number) for number in line.split(" ")] for line in file.read().split("\n")]
count = 0
for value in values:
    difference = value
    while difference[-1] !=0:
        oldDifference = difference.copy()
        count += difference[-1]
        difference = []
        for i in range(len(oldDifference)-1):
            difference.append(oldDifference[i+1]-oldDifference[i])
    print(value,count)
    count = 0