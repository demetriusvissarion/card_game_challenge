import sys
# sys.exit()
import random

from card import Card
from player import Player

class Hand():
    def __init__(self):
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.numbers = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.player_names = ['Player_1', 'Player_2', 'Player_3', 'Player_4']

        # list of player objects:
        self.players = []

        self.deck = []

        self.players_order = []

        # keep a record of the number of rounds (tricks) played for display
        self.trick_counter = 0

        # 'trick' stores cards played during this round (trick) by each player
        self.trick = {'Player_1': '', 'Player_2': '', 'Player_3': '', 'Player_4': ''}

        self.trick_starter = ''
        self.trick_winner = ''
        self.hand_winner = None
        self.score = {'Player_1': 0, 'Player_2': 0, 'Player_3': 0, 'Player_4': 0}
    
    def create_deck(self):
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append(Card(number,suit))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def create_players(self):
        for name in self.player_names:
            self.players.append(Player(name))
    
    def deal_cards(self):
        for _ in range(13):
            for num in range(4):
                card_dealt = self.deck.pop(0)
                self.players[num].hand.append(card_dealt)

    def show_hand(self, player_index):
        hand = [card.name for card in self.players[player_index].hand]
        print(hand)

    def decide_play_order(self):
        if self.trick_counter == 0:
            for player in self.players:
                hand = [card.name for card in player.hand]
                if '2♣' in hand:
                    self.trick_starter = player.name
        else:
            self.trick_starter = self.trick_winner
        
        self.trick_counter += 1
        return self.trick_starter
    
    def user_card_selection(self, valid_selections):
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
        
        return selected_card
    
    def user_plays_card(self):
        print('Player_1, select a card to play: ')
        player_1 = self.players[0]
        player_1_hand = [card.name for card in player_1.hand]
        valid_selections = {}

        # players[Player(hand(card1, card2, card3...)), Player(...), Player(...), Player(...)]

        if '2♣' in player_1_hand:
            print('Note: you have the 2♣ so that is the only card you can play')
            for card in player_1_hand:
                if card == '2♣':
                    print(f'Type {player_1_hand.index(card)} and \"Enter\" to play card {card}')
                    card_number = player_1_hand.index(card)
                    valid_selections[card_number] = card
            selected_card = int(input("Your selection: "))
            selected_card = self.user_card_selection(valid_selections)
        else:
            # if trick exists: 
            if self.trick:
                for card in player_1_hand:
                        # if same suit card(s) in hand,limit possible selections to that
                        if card[-1] in self.trick[self.trick_starter]:
                            card_number = player_1_hand.index(card)
                            valid_selections[card_number] = card
                    
            # if trick doesn't exist choose randomly from all cards
            if not valid_selections:
                for card in player_1_hand:
                    card_number = player_1_hand.index(card)
                    valid_selections[card_number] = card 

            # print valid card selections (can make this seperate function)
            for card_number, card in valid_selections.items():             
                print(f'Type {card_number} and \"Enter\" to play card {card}')

            # exception handling and validation
            selected_card = self.user_card_selection(valid_selections)

        self.trick[player_1.name] = player_1_hand[selected_card]
        print(f'You played: {player_1_hand[selected_card]}')

        # remove the selected card from the hand
        player_1_hand.remove(player_1_hand[selected_card])
        print(f'Player_1, your hand is now: {player_1_hand}')

    def computer_plays_card(self, player):
        player_hand = [card.name for card in player.hand]
        print(f'<dev> {player.name} hand is: ', player_hand)
        # 2 of clubs owner goes first and plays that card first
        if '2♣' in player_hand:
            self.trick[player.name] = '2♣'
            bot_card = '2♣'

        else:
            # if trick exists:                        
            valid_selections = {}
            if self.trick:
                # if same suit cards in hand choose randomly from those cards
                for card in player_hand:
                    if card[-1] in self.trick[self.trick_starter]:
                        card_number = player_hand.index(card)
                        valid_selections[card_number] = card                     
                    
            # else choose randomly from all cards
            if not valid_selections:
                for card in player_hand:
                    card_number = player_hand.index(card)
                    valid_selections[card_number] = card 

            bot_card = random.sample(list(valid_selections.values()), 1)[0]
        
        bot_card_index = player_hand.index(bot_card)
        player_hand.remove(player_hand[bot_card_index - 1])
        self.trick[player.name] = bot_card
        print(f'{player.name} played the card: {bot_card}')

    def play_hand(self):
        self.trick_counter += 1
        first_player_index = self.player_names.index(self.trick_starter)
        self.players_order = self.player_names[(first_player_index):] + self.player_names[:(first_player_index)]
        string_players_order = [player for player in self.players_order]
        print('The players order for this trick is: ', string_players_order)

        for player in self.players_order:
            # User plays a card (Player_1)
            if player == 'Player_1':
                self.user_plays_card()

            # Computer bot plays a card (Player_2, Player_3, Player_4)
            else:
                self.computer_plays_card(player)
        # return self.trick
    
    def decide_trick_winner(self):
        # use player.cards_won to calculate self.hand_winner
        for player in self.players:
            for card in player.cards_won:
                if card == 'Q♠':
                    self.score[player.name] += 13
                elif card[-1] == '♥':
                    self.score[player.name] += 1
        self.trick_winner = self.find_winner()

    def find_winner(self):
        min_score = 999
        winner = None
        for player, points in self.score.items():
            if points < min_score:
                min_score = points
                winner = player
        return winner


    def start_hand(self):
        self.create_deck()
        self.shuffle()
        print('Cards shuffled')
        self.create_players()
        self.deal_cards()

        print('Cards dealt')
        print('Hand has started!')
        print('You are Player_1')
        print('Your hand is:')
        self.show_hand(0)

        # start loop for 13 tricks here
        for _ in range(13):
            self.decide_play_order()
            if self.trick_starter == 'Player_1':
                print(f'You have the 2♣ so you start the first trick')
            else:
                print(f'{self.trick_starter} has the 2♣ so he starts the first trick')
            self.play_hand()
            print('Trick is: ', self.trick)
            self.decide_trick_winner()
            if self.trick_counter < 13:
                print(f'Trick won by {self.trick_winner}, he will start the next trick')
            else:
                print(f'Last trick won by {self.trick_winner}')
        # end loop for 13 tricks here
                
        print(f'Hand won by {self.hand_winner}')

# test_hand1.score = {'Player_1': 100, 'Player_2': 0, 'Player_3': 0, 'Player_4': 14}

# right now I have a while loop that runs while the score of any of the players is smaller than 100, but I want to check also if there is only 1 player with the minimum score, so change my code:

# while score_board.total_score['Player_1'] < 100 and score_board.total_score['Player_2'] < 100 and score_board.total_score['Player_3'] < 100 and score_board.total_score['Player_4'] < 100:
#     new_hand = Hand()
#     new_hand.start_hand()
#     # save hand.score to the ScoreBoard class
#     score_board.hands_score.append(new_hand.score)
#     print(f'Hand won by {new_hand.hand_winner}')
#     score_board.score_table()