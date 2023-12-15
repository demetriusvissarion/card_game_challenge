########### PHASE ONE
# Create a Card class: 
# - generates an instance of each card
# - allows cards to be shuffled
# - allows cards to be dealt to 4 players (remember which cards where played)
#
# Concept of a "hand" is created for a Player
# The "hand" can be printed to the terminal (create a show_hand() function within the class ???)

########### PHASE TWO
# - ability to play cards: 13 "tricks" (rounds) => so deal 13 cards/player at start
# - user can choose what card to play from their own hand => remove chosen card from hand
# - bot payed cards chosen randomly
# - forming of "tricks" - 4 cards, 1 from each player
# - decide each "trick" winner and save the cards to his stack 

########### PHASE THREE
# - 2 Clubs owner goes first and plays that card first

# - players must follow suit
# - tricks are won by the player with the highest card of the leading suit
# - player who won the trick plays first card of next trick

import sys
# sys.exit()
import random


class Card():
    def __init__(self):
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.players = ['Player_1', 'Player_2', 'Player_3', 'Player_4']
        self.deck = []
        self.dealt_hands = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        self.players_order = []
        # keep a record of the number of rounds (tricks) played for display
        self.trick_counter = 0
        # 'trick' stores cards played during this round (trick) by each player
        self.trick = {'Player_1': '', 'Player_2': '', 'Player_3': '', 'Player_4': ''}
        self.points = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        self.trick_starter = ''
        self.trick_winner = ''
    
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
            for num in range(0, 13):
                card_dealt = self.deck.pop(0)
                self.dealt_hands[key].append(card_dealt)
        return self.deck
    
    def show_hand(self):
        string = str(self.dealt_hands['Player_1'])[1:-1]
        print(string)

    def decide_play_order(self):
        if self.trick_counter == 0:
            for player, hand in self.dealt_hands.items():
                if '2♣' in hand:
                    self.trick_starter = player
        else:
            self.trick_starter = self.trick_winner
        return self.trick_starter
    
    def user_plays_card(self):
        player = 'Player_1'
        print('Player_1, select a card to play: ')

        if '2♣' in self.dealt_hands[player]:
            print('Note: you have the 2♣ so that is the only card you can play')
            for card in self.dealt_hands[player]:
                if card == '2♣':
                    print(f'Type {self.dealt_hands[player].index(card)} and \"Enter\" to play card {card}')
            selected_card = int(input("Your selection: "))

        # if trick exists: 
        valid_selections = {}
        if self.trick:
            for card in self.dealt_hands[player]:
                    # if same suit card(s) in hand,limit possible selections to that
                    if card[-1] in self.trick[self.trick_starter]:
                        card_number = self.dealt_hands[player].index(card)
                        valid_selections[card_number] = card
                
        # if trick doesn't exist choose randomly from all cards
        if not valid_selections:
            for card in self.dealt_hands[player]:
                card_number = self.dealt_hands[player].index(card)
                valid_selections[card_number] = card 

        # print valid card selections (can make this seperate function)
        for card_number, card in valid_selections.items():             
            print(f'Type {card_number} and \"Enter\" to play card {card}')

        # exception handling and validation
        while True:
            try:
                selected_card = int(input("Your selection: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                #better try again... return to the start of the loop
                continue
            if selected_card not in list(valid_selections.keys()):
                print("Not an appropriate choice.")
                continue
            else:
                #we're ready to exit the loop.
                break

        self.trick[player] = self.dealt_hands[player][selected_card]
        print(f'You played: {self.dealt_hands[player][selected_card]}')

        # remove the selected card from the hand
        self.dealt_hands[player].remove(self.dealt_hands[player][selected_card])
        print(f'Player_1, your hand is now: {self.dealt_hands[player]}')

    def computer_plays_card(self, player):
        print(f'{player} hand is: ', self.dealt_hands[player])
        # 2 of clubs owner goes first and plays that card first
        if '2♣' in self.dealt_hands[player]:
            # mandatory_card = int(self.dealt_hands[player].index('2♣'))
            self.trick[player] = '2♣'
            bot_card = '2♣'

        else:
            # if trick exists:                        
            valid_selections = {}
            if self.trick:
                # if same suit cards in hand choose randomly from those cards
                for card in self.dealt_hands[player]:
                    if card[-1] in self.trick[self.trick_starter]:
                        card_number = self.dealt_hands[player].index(card)
                        valid_selections[card_number] = card                     
                    
            # else choose randomly from all cards
            if not valid_selections:
                for card in self.dealt_hands[player]:
                    card_number = self.dealt_hands[player].index(card)
                    valid_selections[card_number] = card 

            bot_card = random.sample(list(valid_selections.values()), 1)[0]
        
        bot_card_index = self.dealt_hands[player].index(bot_card)
        self.dealt_hands[player].remove(self.dealt_hands[player][bot_card_index - 1])
        self.trick[player] = bot_card
        print(f'{player} played the card: {bot_card}')

    def play_hand(self):
        self.trick_counter += 1
        first_player_index = self.players.index(self.trick_starter)
        # print(f'first_player_index: {first_player_index}')
        self.players_order = self.players[(first_player_index):] + self.players[:(first_player_index)]
        print('The players order for this trick is: ', self.players_order)

        for player in self.players_order:
            # User plays a card (Player_1)
            if player == 'Player_1':
                self.user_plays_card()

            # Computer bot plays a card
            else:
                self.computer_plays_card(player)

        return self.trick
    
    def decide_trick_winner(self):
        # compare cards played to decide winner
        # save "trick" cards to winner in the "tricks" dictionary
        # save winner name in self.trick_winner

        # for testing purposes I'm setting the winner of the first trick as Player_1
        self.trick_winner = "Player_1"
        return self.trick_winner


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
        self.decide_play_order()
        if self.trick_starter == 'Player_1':
            print(f'You have the 2♣ so you start the first trick')
        else:
            print(f'{self.trick_starter} has the 2♣ so he starts the first trick')
        self.play_hand()
        print('Trick is: ', self.trick)
        # self.trick
        self.decide_trick_winner()
        print(f'Trick won by {self.trick_winner}')



new_game = Card()
new_game.start_game()
# print('Dealt hands: ', new_game.dealt_hands)