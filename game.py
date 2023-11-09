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
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.players = ['Player_1', 'Player_2', 'Player_3', 'Player_4']
        self.deck = []
        self.dealt_hands = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        # self.trick = {'Player_1': '', 'Player_2': '', 'Player_3': '', 'Player_4': ''}
        # self.tricks = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
    
    def create_deck(self):
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(card + suit)
        return self.deck


    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    # cards_dealt set as default to 2 until full game rules applied
    def deal_cards(self, cards_dealt = 2):
        for key in self.dealt_hands:
            for num in range(0, cards_dealt):
                card_dealt = self.deck.pop(0)
                self.dealt_hands[key].append(card_dealt)

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

    # def play_hand(self):
    #     print('Select card to play: ')
    #     counter  = 1
    #     for card in self.dealt_hands['Player_1']:
    #         print(f'Press key {counter} and Enter for card {card}')
    #         counter += 1
    #     selected_card = input("Your selection: ")
    #     if selected_card == 1:
    #         self.trick['Player_1'] = self.dealt_hands['Player_1'][0]
    #     elif selected_card == 2:
    #         self.trick['Player_1'] = self.dealt_hands['Player_1'][1]
    
    # def bot_play(self):
    #     counter = 2
    #     for player in range(counter, 5):
    #         bot_card = random.sample(self.dealt_hands['Player_' + counter], 1)
    #         self.trick['Player_' + counter] = bot_card
    
    # def decide_trick_winner(self):
    #     # compare cards played, decide winner, save to "tricks" dictionary




new_game = Card()
new_game.start_game()
# print('Dealt hands: ', new_game.dealt_hands)