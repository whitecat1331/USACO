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

    def get_card(self, i):
        return self.deck[i]
    
    def add_card(self, card):
        self.deck.append(card)
            
    def print_cards(self):
        for card in self.deck:
            card.print_card_info()


class Player():
    def __init__(self, name):
        self.deck = Deck()
        self.name = name

    def add_card(self, card):
        self.deck.add_card(card)

    def print_cards(self):
        sys.stdout.write(f"\nPlayer: {self.name}\n")
        self.deck.print_cards()


class PokerRulesBook:
    def __init__(self, player1, player2, cards_per_game):
        self.player1 = player1 
        self.player2 = player2
        self.cards_per_game = cards_per_game
        self.all_players = (player1, player2)
        self.games = []
        self.split_games()

    def split_games(self):
        for player in self.all_players:
            current_game_cards = []

            for i in range(self.cards_per_game):
                if (len(current_game_cards) % self.cards_per_game) == 0:
                    self.games.append(current_game_cards)
                    current_game_cards = []
                current_game_cards.append(player.deck.get_card(i))

    def print_cards(self):
        for player in self.all_players:
            player.print_cards()

    def print_games(self):
        game_count = 0
        for game in self.games:
            sys.stdout.write(f"Game: {game_count}: {game}")
            game_count += 1



class PokerHandsSolution:
    def __init__(self, input_file):
        self.player1 = Player("Black")
        self.player2 = Player("White")
        self.input_file = input_file
        self.all_players = (self.player1, self.player2)
        self.read_input_file()

    def read_input_file(self):
        with open(self.input_file, 'r') as f:
            for hands in f:
                line_of_cards = hands.split()
                card_count = 0
                for input_card in line_of_cards:
                    card = Card(input_card[0],input_card[1])
                    if (card_count % 10) < 5:
                        self.player1.add_card(card)
                    else:
                        self.player2.add_card(card)

                    card_count += 1
            
    def testing(self):
        for player in self.all_players:
            player.print_cards()
            sys.stdout.write('\n')
        poker_rule_book = PokerRulesBook(self.player1, self.player2, 5)
        poker_rule_book.print_games()

            







INPUT_FILE = "sample_input.txt"
poker_hands_solution = PokerHandsSolution(INPUT_FILE)    
poker_hands_solution.testing()




