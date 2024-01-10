import itertools as iter

def contiguous(springRange):
    return [(spring[1] - spring[0]) for spring in springRange]

def springRanges(springs):
    unknown = []
    springRange= []
    start = -1
    end = -1
    count = 0
    for i,s in enumerate(springs):
        if s == "#":
            count +=1
            if start == -1:
                start = i
        elif s != "#" and  end == -1 and start != -1:
            end  = i
            springRange.append((start,end))
            start = -1
            end = -1
        if s == "?":
            unknown.append(i)
    if start != -1:
        springRange.append((start,len(springs)))
    return unknown,springRange,count

def addSpring(springRange,index):
    join = []
    for spring in springRange:
        if index == spring[0]-1:
            join.append((0,spring))
        elif index == spring[1]:
            join.append((1,spring))
    if len(join) == 0:
        springRange.append((index,index+1))
    elif len(join) == 1:
        springRange.remove(join[0][1])
        if join[0][0] == 0:
            springRange.append((index,join[0][1][1]))
        else:
            springRange.append((join[0][1][0],index+1))
    else:
        springRange.remove(join[0][1])
        springRange.remove(join[1][1])
        springRange.append((join[0][1][0],join[1][1][1]))
    return sorted(springRange, key=lambda x: x[0])

def tryCombinations(indiciesList,springRange,count):
    i = 0
    for indicies in indiciesList:
        newSpringRange = springRange.copy()
        for index in indicies:
            newSpringRange = addSpring(newSpringRange,index)
        if valid(newSpringRange,count):
            i+=1
    return i

def valid(springRange,count):
    if contiguous(springRange) == count:
        return True
    return False

file = open("input.txt", "r")
i = 0
for j,line in enumerate(file.read().split("\n")):
    springs,count = line.split(" ")
    springs = list(springs)
    count = [int(c) for c in count.split(",")]
    unknown,springRange,hashNo = springRanges(springs)
    fillCount = sum(count) - hashNo
    indicies = iter.combinations(unknown,fillCount)
    i += tryCombinations(list(indicies),springRange,count)
print(i)