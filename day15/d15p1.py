def value(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

text = open("input.txt").read().split(",")
print(sum([value(string) for string in text]))