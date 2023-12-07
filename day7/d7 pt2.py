from collections import Counter 
def cardValue(card):
    value = {'A':13,'K':12,'Q':11,'J':1,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    score = sum([value[card[i]]*14**(5-i) for i,e in enumerate(card)])
    return score

def handScore(hand):
    cards = Counter(hand[0])
    cards['J'] = 0
    del cards['J']
    count = sorted(list(cards.values()))
    if count == [5] or count == [] or len(count) == 1:
        return (7,hand)
    elif count == [1,4] or count == [1,1] or count == [1,3] or count == [1,2]:
        return (6,hand)
    elif count == [2,3] or count == [2,2]:
        return (5,hand)
    elif count == [1,1,3] or count == [1,1,1] or count == [1,1,2]:
        return (4,hand)
    elif count == [1,2,2]:
        return (3,hand)
    elif count == [1,1,1,2] or count == [1,1,1,1]:
        return (2,hand)
    elif count == [1,1,1,1,1]:
        return (1,hand)

file = open("day7/input.txt", "r")
text = file.read()
hands = [line.split(" ") for line in text.split('\n')]
hands = [handScore(hand) for hand in hands]
hands = sorted(hands, key=lambda element: (element[0], cardValue(element[1][0])))
score = sum([(i+1)*int(x[1][1]) for i,x in enumerate(hands)])
print(score)