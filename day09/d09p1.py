file = open("input.txt", "r")
values = [[int(number) for number in line.split(" ")] for line in file.read().split("\n")]
count = 0
for value in values:
    while any(value):
        count += value[-1]
        value  = [first - second for (first, second) in zip(value[1:], value)]
print(count)