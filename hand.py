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
        self.hearts_are_broken = False
    
    def create_deck(self):
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append(Card(number,suit))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def create_players(self):
        for name in self.player_names:
            self.players.append(Player(name))

    def sort_cards(self):
        suit_order = {'♥': 0, '♠': 1, '♦': 2, '♣': 3}
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        def get_card_sort_key(card):
            suit_key = suit_order.get(card.name[-1], len(suit_order))
            value_key = card_values.get(card.name[:-1], 0)
            return suit_key, value_key, card.name

        for player in self.players:
            player.hand = sorted(player.hand, key=get_card_sort_key)
    
    def deal_cards(self):
        for _ in range(13):
            for num in range(4):
                card_dealt = self.deck.pop(0)
                self.players[num].hand.append(card_dealt)
        self.sort_cards()
    
    def pass_three_cards(self, hand_counter):
        valid_selections = {}

        # Hand 1: pass 3 cards to the opponent on your right: (the one before you, example player_2 passes to player_1)
        if hand_counter == 1:
            # Player_1:
            # pass 3 cards to right player (-1)
            print('Select 3 cards from your hand to pass to the player on your right')
            for card in self.players[0].hand:
                card_index = self.players[0].hand.index(card)
                valid_selections[card_index] = card           
                print(f'Type {card_index} and \"Enter\" to play card {card.name}')
            print('Select the first card')
            first_selection_index = self.user_card_selection(valid_selections)
            print('Select the second card')
            second_selection_index = self.user_card_selection(valid_selections)
            print('Select the third card')
            third_selection_index = self.user_card_selection(valid_selections)
            player_1_selected_cards = [self.players[0].hand[first_selection_index], self.players[0].hand[second_selection_index], self.players[0].
            hand[third_selection_index]]
            print(f'Cards {[card.name for card in player_1_selected_cards]} will be passed to Player_4')
            player = self.players[0]
            # remove selected cards from hand
            for card in player_1_selected_cards:
                self.remove_played_card(player, card.name)

            # Player_2:
            # select 3 random cards to pass (later change this to make the game harder)
            player_2 = self.players[1]
            player_2_hand = self.players[1].hand
            player_2_selected_cards = random.sample(player_2_hand, 3)
            # remove selected cards from hand
            for card in player_2_selected_cards:
                self.remove_played_card(player_2, card.name)

            # Player_3:
            # select 3 random cards to pass (later change this to make the game harder)
            player_3 = self.players[2]
            player_3_hand = self.players[2].hand
            player_3_selected_cards = random.sample(player_3_hand, 3)
            # remove selected cards from hand
            for card in player_3_selected_cards:
                self.remove_played_card(player_3, card.name)

            # Player_4:
            # select 3 random cards to pass (later change this to make the game harder)
            player_4 = self.players[3]
            player_4_hand = self.players[3].hand
            player_4_selected_cards = random.sample(player_4_hand, 3)
            # remove selected cards from hand
            for card in player_4_selected_cards:
                self.remove_played_card(player_4, card.name)
            
            # add all players selected cards to the previous player hand
            # Player_1 => Player_4
            for card in player_1_selected_cards:
                self.players[3].hand.append(card)
            # Player_2 => Player_1
            for card in player_2_selected_cards:
                self.players[0].hand.append(card)
            print(f'Player_1 you received cards {[card.name for card in player_2_selected_cards]} from Player_2')
            # Player_3 => Player_2
            for card in player_3_selected_cards:
                self.players[1].hand.append(card)
            # Player_4 => Player_3
            for card in player_4_selected_cards:
                self.players[2].hand.append(card)
            
            self.sort_cards()
            valid_selections = {}
                
        # Hand 2: pass 3 cards to the opponent on your left: (the one after you, example player_2 passes to player_3)
        if hand_counter == 2:
            # Player_1:
            # pass 3 cards to left player (+1)
            print('Select 3 cards from your hand to pass to the player on your left')
            for card in self.players[0].hand:
                card_index = self.players[0].hand.index(card)
                valid_selections[card_index] = card           
                print(f'Type {card_index} and \"Enter\" to play card {card.name}')
            print('Select the first card')
            first_selection_index = self.user_card_selection(valid_selections)
            print('Select the second card')
            second_selection_index = self.user_card_selection(valid_selections)
            print('Select the third card')
            third_selection_index = self.user_card_selection(valid_selections)
            player_1_selected_cards = [self.players[0].hand[first_selection_index], self.players[0].hand[second_selection_index], self.players[0].
            hand[third_selection_index]]
            print(f'Cards {[card.name for card in player_1_selected_cards]} will be passed to Player_2')
            player = self.players[0]
            # remove selected cards from hand
            for card in player_1_selected_cards:
                self.remove_played_card(player, card.name)

            # Player_2:
            # select 3 random cards to pass (later change this to make the game harder)
            player_2 = self.players[1]
            player_2_hand = self.players[1].hand
            player_2_selected_cards = random.sample(player_2_hand, 3)
            # remove selected cards from hand
            for card in player_2_selected_cards:
                self.remove_played_card(player_2, card.name)

            # Player_3:
            # select 3 random cards to pass (later change this to make the game harder)
            player_3 = self.players[2]
            player_3_hand = self.players[2].hand
            player_3_selected_cards = random.sample(player_3_hand, 3)
            # remove selected cards from hand
            for card in player_3_selected_cards:
                self.remove_played_card(player_3, card.name)

            # Player_4:
            # select 3 random cards to pass (later change this to make the game harder)
            player_4 = self.players[3]
            player_4_hand = self.players[3].hand
            player_4_selected_cards = random.sample(player_4_hand, 3)
            # remove selected cards from hand
            for card in player_4_selected_cards:
                self.remove_played_card(player_4, card.name)
            
            # add all players selected cards to the next player hand
            # Player_1 => Player_2
            for card in player_1_selected_cards:
                self.players[1].hand.append(card)
            # Player_2 => Player_3
            for card in player_2_selected_cards:
                self.players[2].hand.append(card)
            # Player_3 => Player_4
            for card in player_3_selected_cards:
                self.players[3].hand.append(card)
            # Player_4 => Player_1
            for card in player_4_selected_cards:
                self.players[0].hand.append(card)
            print(f'Player_1 you received cards {[card.name for card in player_4_selected_cards]} from Player_4')
            
            self.sort_cards()
            valid_selections = {}

        # Hand 3: pass 3 cards to the opponent in front of you: (the one not after you or before you, example player_2 passes to player_4)
        if hand_counter == 3:
            # Player_1:
            # pass 3 cards to front player (-2 / +2)
            print('Select 3 cards from your hand to pass to the player in front of you')
            for card in self.players[0].hand:
                card_index = self.players[0].hand.index(card)
                valid_selections[card_index] = card           
                print(f'Type {card_index} and \"Enter\" to play card {card.name}')
            print('Select the first card')
            first_selection_index = self.user_card_selection(valid_selections)
            print('Select the second card')
            second_selection_index = self.user_card_selection(valid_selections)
            print('Select the third card')
            third_selection_index = self.user_card_selection(valid_selections)
            player_1_selected_cards = [self.players[0].hand[first_selection_index], self.players[0].hand[second_selection_index], self.players[0].
            hand[third_selection_index]]
            print(f'Cards {[card.name for card in player_1_selected_cards]} will be passed to Player_3')
            player = self.players[0]
            # remove selected cards from hand
            for card in player_1_selected_cards:
                self.remove_played_card(player, card.name)

            # Player_2:
            # select 3 random cards to pass (later change this to make the game harder)
            player_2 = self.players[1]
            player_2_hand = self.players[1].hand
            player_2_selected_cards = random.sample(player_2_hand, 3)
            # remove selected cards from hand
            for card in player_2_selected_cards:
                self.remove_played_card(player_2, card.name)

            # Player_3:
            # select 3 random cards to pass (later change this to make the game harder)
            player_3 = self.players[2]
            player_3_hand = self.players[2].hand
            player_3_selected_cards = random.sample(player_3_hand, 3)
            # remove selected cards from hand
            for card in player_3_selected_cards:
                self.remove_played_card(player_3, card.name)

            # Player_4:
            # select 3 random cards to pass (later change this to make the game harder)
            player_4 = self.players[3]
            player_4_hand = self.players[3].hand
            player_4_selected_cards = random.sample(player_4_hand, 3)
            # remove selected cards from hand
            for card in player_4_selected_cards:
                self.remove_played_card(player_4, card.name)
            
            # add all players selected cards to the next player hand
            # Player_1 => Player_3
            for card in player_1_selected_cards:
                self.players[2].hand.append(card)
            # Player_2 => Player_4
            for card in player_2_selected_cards:
                self.players[3].hand.append(card)
            # Player_3 => Player_1
            for card in player_3_selected_cards:
                self.players[0].hand.append(card)
            print(f'Player_1 you received cards {[card.name for card in player_4_selected_cards]} from Player_4')
            # Player_4 => Player_2
            for card in player_4_selected_cards:
                self.players[1].hand.append(card)
            
            self.sort_cards()
            valid_selections = {}

        # Hand 4: don't pass any cards
        if hand_counter == 4:
            # don't pass any cards
            pass


    def show_hand(self, player_index):
        player_hand = self.players[player_index].hand
        cards_in_hand = [card.name for card in player_hand]
        return cards_in_hand

    def decide_play_order(self):
        if self.trick_counter == 0:
            for player in self.players:
                hand = [card.name for card in player.hand]
                if '2♣' in hand:
                    self.trick_starter = player.name
        else:
            self.trick_starter = self.trick_winner
        
        return self.trick_starter
    
    def user_card_selection(self, valid_selections):
        # exception handling and validation
        while True:
            try:
                selected_card_index = int(input("Your selection: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                #better try again... return to the start of the loop
                continue
            if selected_card_index not in list(valid_selections.keys()):
                print("Not an appropriate choice.")
                continue
            else:
                #we're ready to exit the loop.
                break
        
        return selected_card_index
    
    def remove_played_card(self, player, card_to_remove):
        player_index = self.player_names.index(player.name)
        # print('player: ', player)
        self.players[player_index].hand = [card for card in self.players[player_index].hand if card.name != card_to_remove]

    def reset_trick(self):
        self.trick = {'Player_1': '', 'Player_2': '', 'Player_3': '', 'Player_4': ''}
    
    def user_plays_card(self, player):
        print('Player_1, select a card to play: ')
        player_1 = player
        player_1_hand = [card.name for card in player_1.hand]
        valid_selections = {}

        if '2♣' in player_1_hand:
            print('Note: you have the 2♣ so that is the only card you can play')
            for card in player_1_hand:
                if card == '2♣':
                    print(f'Type {player_1_hand.index(card)} and \"Enter\" to play card {card}')
                    card_number = player_1_hand.index(card)
                    valid_selections[card_number] = card
            selected_card_index = self.user_card_selection(valid_selections)
        else:
            # if trick has at least one value (it means another player started the trick): 
            if any(value for value in self.trick.values()):
                for card in player_1_hand:
                        # if same suit card(s) in hand,limit possible selections to that
                        if card[-1] in self.trick[self.trick_starter]:
                            card_number = player_1_hand.index(card)
                            valid_selections[card_number] = card
            
            # if trick has at least one value and not "Hearts are broken"
            if any(value for value in self.trick.values()) and not self.hearts_are_broken:
                for card in player_1_hand:
                        # if same suit card(s) in hand,limit possible selections to that
                        if card[-1] in self.trick[self.trick_starter] and card[-1] != '♥':
                            card_number = player_1_hand.index(card)
                            valid_selections[card_number] = card

            # if no self.trick or no same suit card(s) in hand, choose randomly from all cards (if heart played here it will trigger "Hearts are broken")
            if not valid_selections:
                for card in player_1_hand:
                    card_number = player_1_hand.index(card)
                    valid_selections[card_number] = card

            # print('valid_selections: ', valid_selections)

            # print valid card selections (can make this seperate function)
            for card_number, card in valid_selections.items():             
                print(f'Type {card_number} and \"Enter\" to play card {card}')

            # exception handling and validation
            selected_card_index = self.user_card_selection(valid_selections)

        selected_card = player_1_hand[selected_card_index]
        self.trick[player_1.name] = selected_card
        print(f'You played: {selected_card}')
        if selected_card[-1] == '♥' and not self.hearts_are_broken:
            print("Hearts are broken!")
            self.hearts_are_broken = True

        # remove the selected card from the hand
        self.remove_played_card(player_1, selected_card)
        # self.reset_trick()

    def computer_plays_card(self, player):
        player_hand = [card.name for card in player.hand]
        # print(f'<dev> {player.name} hand is: ', player_hand)
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
                # if                 
                    
            # if no self.trick choose randomly from all cards
            if not valid_selections:
                for card in player_hand:
                    card_number = player_hand.index(card)
                    valid_selections[card_number] = card 

            # change bot_card selection to improve bot play (min() or  )
            bot_card = random.sample(list(valid_selections.values()), 1)[0]

        self.trick[player.name] = bot_card
        print(f'{player.name} played the card: {bot_card}')
        
        self.remove_played_card(player, bot_card)

    def play_hand(self):
        self.trick_counter += 1
        first_player_index = self.player_names.index(self.trick_starter)
        self.players_order = self.player_names[(first_player_index):] + self.player_names[:(first_player_index)]
        string_players_order = [player for player in self.players_order]
        print('The players order for this trick is: ', string_players_order)

        for player in self.players_order:
            # User plays a card (Player_1)
            if player == 'Player_1':
                player_object = next((obj for obj in self.players if obj.name == player), None)
                self.user_plays_card(player_object)

            # Computer bot plays a card (Player_2, Player_3, Player_4)
            else:
                player_object = next((obj for obj in self.players if obj.name == player), None)
                self.computer_plays_card(player_object)
        self.trick_counter += 1
                
    def card_value(self, card):
        # order of card values for comparison
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        # get card value from the card string
        value = card[:-1]

        # return the numeric value
        return card_values.get(value, 0)
    
    def reset_score(self):
        self.score = {'Player_1': 0, 'Player_2': 0, 'Player_3': 0, 'Player_4': 0}
    
    def calculate_score(self):
        self.reset_score()
        # print('Before calculations self.score: ', self.score)
        # use player.cards_won to calculate score
        # if none of the players has all 13 hearts and the Q♠ (26 points total)
        for player in self.players:
            # print(f'{player.name} cards_won: {player.cards_won}')
            # print('player.name: ', player.name)
            # print('before self.score[player.name]: ', self.score[player.name])
            for card in player.cards_won:
                if card == 'Q♠':
                    # print('<dev> Q♠ hit')
                    self.score[player.name] += 13
                elif card[-1] == '♥':
                    # print('<dev> ♥ hit')
                    self.score[player.name] += 1
            # print('after self.score[player.name]: ', self.score[player.name])
        
    # find trick winner and save score
    def decide_trick_winner(self):
        trick_cards = self.trick.values()

        # find the suit of the card played by the trick starter
        starter_card = self.trick[self.trick_starter]
        starter_suit = starter_card[-1]

        same_suit_cards = [card for card in trick_cards if card[-1] == starter_suit]
        highest_card = max(same_suit_cards, key=self.card_value)
        self.trick_winner = [player for player, card in self.trick.items() if card == highest_card][0]

        # save trick to player.cards_won
        for player, card in self.trick.items():
            trick_winner_index = self.player_names.index(self.trick_winner)
            self.players[trick_winner_index].cards_won.append(card)

    def decide_hand_winner(self):
        min_score = 999
        for player, points in self.score.items():
            if points < min_score:
                min_score = points
                self.hand_winner = player
        return self.hand_winner

    def start_hand(self, hand_counter):
        # print('self.score: ', self.score)
        self.create_deck()
        self.shuffle()
        print('Cards shuffled')
        self.create_players()
        self.deal_cards()
        print('Cards dealt')

        self.pass_three_cards(hand_counter)

        print('Hand has started!')
        print('You are Player_1')

        # start loop for 13 tricks here
        for _ in range(13):
            print('Your hand is: ', self.show_hand(0))
            # print('<dev> Player_2 hand is: ', self.show_hand(1))
            # print('<dev> Player_3 hand is: ', self.show_hand(2))
            # print('<dev> Player_4 hand is: ', self.show_hand(3))
            self.decide_play_order()
            if self.trick_counter == 0:
                if self.trick_starter == 'Player_1':
                    print(f'You have the 2♣ so you start the first trick')
                else:
                    print(f'{self.trick_starter} has the 2♣ so he starts the first trick')

            self.play_hand()
            print('Trick is: ', self.trick)
            self.decide_trick_winner()
            self.reset_trick()
            if self.trick_counter < 13:
                print(f'Trick won by {self.trick_winner}, he will start the next trick')
            else:
                print(f'Last trick won by {self.trick_winner}')
            self.decide_hand_winner()
        self.calculate_score()
        # end loop for 13 tricks here

# players[Player(hand(card1, card2, card3...)), Player(...), Player(...), Player(...)]
