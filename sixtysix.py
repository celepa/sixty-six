class Card:
    suits = ["spades", "diamonds", "hearts", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

from random import shuffle

class Deck:
    def __init__(self, stripped_deck_card = 2):
        self.cards = []
        for i in range(stripped_deck_card, 15):
            for j in range(0, 4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck(9)
cards_number = 0
while len(deck.cards):
    cards_number+=1
    print(str(cards_number) + " " + str(deck.rm_card()))

