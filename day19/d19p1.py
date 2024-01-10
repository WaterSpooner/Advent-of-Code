import re

def calculate(instructionList,data):
    instruction = "in"
    x,m,a,s = data
    i = instructionList[instruction]
    while True:
        for instruct in i:
            if len(instruct) == 1:
                if instruct[0] == "A":
                    return sum(data)
                elif instruct[0] == "R":
                    return 0
                i = instructionList[instruct[0]]
                break
            if eval(instruct[0]):
                if instruct[1] == "A" or instruct[1] == "R":
                    i = [instruct[1]]
                    break
                i = instructionList[instruct[1]]
                break

instructions,data = [data.split("\n") for data in open("input.txt").read().split("\n\n")]
data = [[int(num) for num in re.sub(r"[^0-9,]", "",d).split(",")] for d in data]
instructionsDict = {}
for instruction in instructions:
    instruction = re.split(r'[{,]', instruction.rstrip("}"))
    instructionList = [i.split(":") for i in instruction]
    instructionsDict[instructionList[0][0]] = instructionList[1:]
total = 0
for d in data:
    total += calculate(instructionsDict,d)
print(total)




