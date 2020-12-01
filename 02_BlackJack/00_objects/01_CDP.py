import random


class Card:

    def __init__(self, value, suit):

        self.value = value
        self.suit = suit

    def show(self):
        print(f'{self.value} of {self.suit}')


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Diamonds', 'Hearts', 'Spades', 'Clubs']:
            for v in ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']:
                self.cards.append(Card(v, s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
