import re
file = open("input.txt", "r")
text = file.read()
text = re.sub(r"[^0-9\s]+", "", text)
text = [[[int(z) for z in y.split(" ")] for y in x.lstrip().split('\n')] for x in re.split(r'\n\n', text)]
numbers = text.pop(0)[0]
output = []
for num in numbers:
    for translation in text:
        for t in translation:
            if num >= t[1] and num < (t[1] + t[2]):
                num = num - t[1] + t[0]
                break
    output.append(num)
print(min(output))
