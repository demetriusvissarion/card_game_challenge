########### PHASE ONE
# Create a Card class: 
# - generates an instance of each card
# - allows cards to be shuffled
# - allows cards to be dealt to 4 players (remember which cards where played)
#
# Concept of a "hand" is created for a Player
# The "hand" can be printed to the terminal (create a show_hand() function within the class ???)

########### PHASE TWO
#
#
#
#
#
#
#
#


import random
class Card():
    def __init__(self):
        self.players = ['Player_1', 'Player_2', 'Player_3', 'Player_4']
        self.deck = []
        self.dealt_hands = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    def create_deck(self):
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(card + suit)
        return self.deck


    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    def deal_cards(self):
        for key in self.dealt_hands:
            self.dealt_hands[key] = self.dealt_hands[key] + random.sample(self.deck, 2)
            # print(self.dealt_hands)
            for card in self.dealt_hands[key]:
                # print(hand)
                if card in self.deck:
                    self.deck.remove(card)
            # print(self.deck)

        return self.deck
    
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
# print('Dealt hands: ', new_game.dealt_hands)