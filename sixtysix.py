from random import shuffle

class Card:
    suits = ["S", "D", "H", "C"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return self.values[self.value] + self.suits[self.suit]

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

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

class Game:
    dealer = 0
    players = []
    def __init__(self):
        self.deck = Deck(9)
        for i in range(0,4):
            self.players.append(Player(i))

    def deal_cards(self):
        while self.deck.cards:
            self.players[0].cards.append(self.deck.rm_card())
            self.players[1].cards.append(self.deck.rm_card())
            self.players[2].cards.append(self.deck.rm_card())
            self.players[3].cards.append(self.deck.rm_card())
    def play_game(self):
        self.deal_cards()
        print("P1: ", end = '')
        for i in range(0, 6):
            print(self.players[0].cards[i], end = ' ')
        print("\nP2: ", end = '')
        for i in range(0, 6):
            print(self.players[1].cards[i], end = ' ')
        print("\nP3: ", end = '')
        for i in range(0, 6):
            print(self.players[2].cards[i], end = ' ')
        print("\nP4: ", end = '')
        for i in range(0, 6):
            print(self.players[3].cards[i], end = ' ')
        

game = Game()
game.play_game()

# deck = Deck(9)
# cards_number = 0
# while len(deck.cards):
#     cards_number+=1
#     print(str(cards_number) + " " + str(deck.rm_card()))

