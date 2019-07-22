import random

cards = [2,3,4,5,6,7,8,9,10,'A','J','Q','K']
suits = ["Spade", "Club", "Heart", "Diamomnd"]
cardDeck = []
tally = 0

class PlayerCard:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def printCard(self):
        print (self.suit + " - " + self.number)

# deck cards are stored in 'cardDeck'. Pull/delete from here and attach to player hand
def countCards():
    global tally
    for s in suits:
        for c in cards:
            newCard = PlayerCard(str(c), s)
            cardDeck.insert(tally, newCard)
            tally+=1
    print ("Total cards in deck: " + str(len(cardDeck)))

countCards()
playerHand = []
randomNumberList = []
numOfRepeatedCards = 0

# draws from length of deck, however no suit + is attached
def drawCardsForPlayer(numerOfCardsToDealToHand):
    randomSuitFound = False
    randomNumberFound = False
    global numOfRepeatedCards
    for x in range(numerOfCardsToDealToHand):
        r1 = random.randint(0, len(cards)-1)
        r2 = random.randint(0, len(suits)-1)
        print ("Random card from list is: " + str(r1, r2)
        # randNumber = random.randint(0, len(cardDeck)-1)
        newNumberFound = False
        while newNumberFound is not True:
            if randNumber in randomNumberList:
                print (str(randNumber) + " is already in the list!!!. Generating a new random number.")
                numOfRepeatedCards+=1
                newNumberFound = False
            if randNumber not in randomNumberList:
                print (str(randNumber) + " is a new number. Adding to the list.")
                randomNumberList.insert(x, randNumber)
                newNumberFound = True
            randNumber = random.randint(0, len(cardDeck)-1)
    print ("Cards generated: " + str(len(randomNumberList)))
    print ("Number of repeated cards: " + str(numOfRepeatedCards))
    print ("Cards remaining in deck: " + str(len(cardDeck) - len(randomNumberList)))
    
drawCardsForPlayer(6)

# need to draw a random string from number list and suit list
# this is the card to be pulled from the card deck list 
