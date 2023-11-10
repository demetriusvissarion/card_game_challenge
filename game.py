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



import random
class Card():
    def __init__(self):
        self.suits = ['♦', '♣', '♥', '♠' ]
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.players = ['Player_1', 'Player_2', 'Player_3', 'Player_4']
        self.deck = []
        self.dealt_hands = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
        self.players_order = []
        self.trick_counter = 0
        self.trick = {'Player_1': '', 'Player_2': '', 'Player_3': '', 'Player_4': ''}
        self.tricks = {'Player_1': [], 'Player_2': [], 'Player_3': [], 'Player_4': []}
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
    
    def deal_cards(self, cards_dealt = 13):
        for key in self.dealt_hands:
            for num in range(0, cards_dealt):
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

    def play_hand(self):
        first_player_index = self.players.index(self.trick_starter)
        # print(f'first_player_index: {first_player_index}')
        self.players_order = self.players[(first_player_index):] + self.players[:(first_player_index)]
        print('The players order for this trick is: ', self.players_order)

        # use players_order list to play the hand
        for player in self.players_order:
            if player == 'Player_1':
                print('Player_1, select a card to play: ')
                if '2♣' in self.dealt_hands['Player_1']:
                    print('Note: you have the 2♣ so that is the only card you can play')
                    for card in self.dealt_hands['Player_1']:
                        if card == '2♣':
                            print(f'Type {self.dealt_hands[player].index(card)} and \"Enter\" to play card {card}')
                    selected_card = int(input("Your selection: "))
                    selected_card = 1
                else:
                    for card in self.dealt_hands['Player_1']:
                        print(f'Type {self.dealt_hands[player].index(card)} and \"Enter\" to play card {card}')
                    selected_card = int(input("Your selection: "))
                self.trick['Player_1'] = self.dealt_hands['Player_1'][selected_card]
                # remove played card from self.dealt_hands
                print(f'You played: {self.dealt_hands["Player_1"][selected_card]}')
                self.dealt_hands['Player_1'].remove(self.dealt_hands['Player_1'][selected_card])
                print(f'Your hand is now: {self.dealt_hands["Player_1"]}')
            else:
                bot_card = random.sample(self.dealt_hands[player], 1)[0]
                print(f'Bot card is: {bot_card}')
                bot_card_index = self.dealt_hands[player].index(bot_card)
                # print(f'Bot card index is: {bot_card_index}')
                # remove played card from self.dealt_hands
                self.dealt_hands[player].remove(self.dealt_hands[player][bot_card_index - 1])

                self.trick[player] = bot_card
        return self.trick,
    
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
        # wrap into a while loop and repeat it until all players hands are exhausted:
        # while len(self.dealt_hands['Player_1']) > 0:
        self.decide_play_order()
        print(f'{self.trick_starter} has the 2♣ so he starts the trick')
        self.play_hand()
        print('Trick is: ', self.trick)
        # self.trick
        self.decide_trick_winner()
        print(f'Trick won by {self.trick_winner}')



new_game = Card()
new_game.start_game()
# print('Dealt hands: ', new_game.dealt_hands)