########### PHASE ONE
# Create a Card class: 
# - generates an instance of each card
# - allows cards to be shuffled
# - allows cards to be dealt to 4 players (remember which cards where played)
#
# Concept of a "hand" is created for a Player
# The "hand" can be printed to the terminal (create a show_hand() function within the class ???)

import random
class Card():
    def __init__(self):
        self.players = ['Player_1', 'Player_2', 'Player_3', 'Player_4']
        self.start_deck = []
        self.shuffeled_deck = []
        self.after_deal_deck = []
        self.dealt_hands = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    def create_deck(self):
        for suit in self.suits:
            for card in self.cards:
                self.start_deck.append(card + suit)
        return self.start_deck


    def shuffle(self):
        random.shuffle(self.start_deck)
        self.shuffeled_deck = self.start_deck
        # print(self.shuffeled_deck)
        return self.shuffeled_deck
    
    def deal_cards(self):
        self.after_deal_deck = self.shuffeled_deck
        for key in self.dealt_hands:
            self.dealt_hands[key] = self.dealt_hands[key] + random.sample(self.shuffeled_deck, 2)
            # print(self.dealt_hands[key])
            for hand in self.dealt_hands[key]:
                for card in hand:
                    if card in self.after_deal_deck:
                        self.after_deal_deck.remove(card)

        return self.after_deal_deck
    
    def show_hand(self):
        string = str(self.dealt_hands['Player_1'])[1:-1]
        print(string)


    def start_game(self):
        self.create_deck()
        self.shuffle()
        print('Cards shuffled')
        self.deal_cards()
        print('Cards dealt')
        print('Game has started!')
        print('You are Player_1')
        print('Your hand is:')
        self.show_hand()

new_game = Card()
new_game.start_game()