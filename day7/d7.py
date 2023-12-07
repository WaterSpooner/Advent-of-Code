import re
cardValue = {'A':12,'K':11,'Q':10,'J':9,'T':8,'9':7,'8':6,'7':5,'6':4,'5':3,'4':2,'3':1,'2':0}    
def greatestHand(hand,amount):
    maxAmount = -1
    maxCard = ''
    for card in hand:
        if hand[card] == amount and maxAmount < cardValue[card]:
            maxCard = card
            maxAmount = cardValue[card]
    return (maxCard,maxAmount)

file = open("day7/input.txt", "r")
text = file.read()
hands = {}
for line in text.split('\n'):
    l = line.split(' ')
    hands[l[0]] = int(l[1]) 
handValues ={}
for hand in hands.keys():
    cards ={}
    for card in hand:
        cards[card] = cards.get(card,0)+1
    for i in range(4,-1,-1):
        value = greatestHand(cards,i)
        if i == 3 and value[0] != '' and greatestHand(cards,i-1)[0] != '':
            handValues[hand] = 4*13 + value[1]
            break
        if value[0] != '':
            handValues[hand] = (i+1)*13 + value[1] if i == 4 else i*13 + value[1]
            break
i= len(hands)
while len(handValues) > 0:
    hand = max(handValues, key=handValues.get)
    hands[hand] =hands[hand] * i
    i-=1
    del handValues[hand]
print(sum(hands.values()))