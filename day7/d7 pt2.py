import re
from collections import Counter
cardValue = {'A':13,'K':12,'Q':11,'J':1,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}    
def greatestHand(hand,amount,secondAmount = -1):
    three = False
    two = False
    pairs = 0
    jokerCount = hand.get('J',0)

    if secondAmount == 2:
        for card in hand.keys():
            if hand[card] == 2:
                pairs +=1
        if pairs == 2:
            return True
        return False
    
    if secondAmount == 3:
        if jokerCount == 1:
            for card in hand.keys():
                if hand[card] == 2 and card != 'J':
                    pairs +=1
            if pairs == 2:
                return True
        else:
            for card in hand.keys():
                if hand[card] == 2:
                    two = True
                if hand[card] == 3:
                    three = True
            return two and three

    for card in hand.keys():
        if card == 'J':
            if hand[card] == amount:
                return True
        else:
            if hand[card]+jokerCount == amount:
                return True        
    return False

def calculateValue(hand,handValue):
    value = 0
    handLen = len(hand)
    for i in range(handLen):
        value += (cardValue[hand[i]]) * (14**(5-i-1))
    value += (handValue) * (14**(handLen))
    return value

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
    validCards = []
    validCards.append(greatestHand(cards,5))
    validCards.append(greatestHand(cards,4))
    validCards.append(greatestHand(cards,2,3))
    validCards.append(greatestHand(cards,3))
    validCards.append(greatestHand(cards,2,2))
    validCards.append(greatestHand(cards,2))
    validCards.append(greatestHand(cards,1))
    score = len(validCards) - validCards.index(True)
    handValues[hand] = calculateValue(hand,score)

i = len(hands)
total = 0
while i > 0:
    hand = max(handValues, key=handValues.get)
    print(i,hand,hands[hand])
    total += hands[hand] * i
    i-=1
    handValues[hand] = -1
print(total)