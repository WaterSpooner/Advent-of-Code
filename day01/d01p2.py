import re
f = open("input.txt", "r")
lines = f.readlines()
count = 0
nums = []
numbers = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
for line in lines:
    numString = re.findall(r'(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))',line)
    num = numbers[numString[0]] + numbers[numString[-1]]
    count += (int(num))
print(count)
