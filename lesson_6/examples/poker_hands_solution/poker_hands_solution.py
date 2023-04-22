import sys


class Card:
    SUITS = ('C', 'D', 'H', 'S')
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_card(self):
        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(Card(value, suit))

    def get_deck(self):
        return self.deck
    
    def get_cards(self):
        for card in self.deck:
            yield card.get_card()

class PokerHand:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

class PokerHandsSolution:
    def __init__(self, file_of_hands):
        with open(file_of_hands, 'r') as f:
            for hands in f:
                all_cards = hands.split()





    

for card in Deck().get_cards():
    print(card)


