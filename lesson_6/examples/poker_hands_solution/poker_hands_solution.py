import sys


class Card:
    SUITS = ('C', 'D', 'H', 'S')
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def print_card_info(self):
        sys.stdout.write(f"{self.value}{self.suit}")


class Deck:
    def __init__(self):
        self.deck = []

    def fill_deck(self):
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.deck.append(Card(value, suit))

    def get_deck(self):
        return self.deck
    
    def add_card(self, card):
        self.deck.append(card)
            
    def print_cards(self):
        for card in self.deck:
            card.print_card_info()

class PokerHand():
    def __init__(self, name):
        self.deck = Deck()
        self.name = name

    def add_card(self, card):
        self.deck.add_card(card)

    def print_cards(self):
        sys.stdout.write(f"\nPlayer: {self.name}\n")
        self.deck.print_cards()


class PokerHandsSolution:
    def __init__(self, file_of_hands):
        player1 = PokerHand("Black")
        player2 = PokerHand("White")
        all_players = (player1, player2)

        with open(file_of_hands, 'r') as f:
            for hands in f:
                line_of_cards = hands.split()
                card_count = 0
                for input_card in line_of_cards:
                    card = Card(input_card[0],input_card[1])
                    if (card_count % 10) < 5:
                        player1.add_card(card)
                    else:
                        player2.add_card(card)

                    card_count += 1
            
        for player in all_players:
            player.print_cards()
        sys.stdout.write('\n')



INPUT_FILE = "sample_input.txt"
poker_hands_solution = PokerHandsSolution(INPUT_FILE)    



