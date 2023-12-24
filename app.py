from hand import Hand
from score_board import ScoreBoard

class App:
    def __init__(self):
        self.score_board = ScoreBoard()
        self.hand_counter = 1

    def run(self):
        # add here while loop to check if any players reached 100 score and if only one player has minimum score
        while not any(self.score_board.total_score[player] >= 1000 for player in self.score_board.total_score) or sum(self.score_board.total_score[player] == min(self.score_board.total_score.values()) for player in self.score_board.total_score) != 1:
            new_hand = Hand()
            new_hand.start_hand(self.hand_counter)
            # save hand.score to the ScoreBoard class
            self.score_board.hands_score.append(new_hand.score)
            print('self.score_board.hands_score: ', self.score_board.hands_score)
            print(f'Hand won by {new_hand.hand_winner}')
            self.score_board.score_table()

            print('Do you want to play another hand? (y/n)')

            # exception handling and validation
            while True:
                try:
                    play_more = input("Your selection: ")
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    #better try again... return to the start of the loop
                    continue
                if play_more not in ['y', 'Y', 'n', 'N']:
                    print("Not an appropriate choice.")
                    continue
                else:
                    #we're ready to exit the loop.
                    break

            if play_more.lower() == 'y':
                print("Ok, starting another hand")
                print('Get ready')
                if self.hand_counter < 4:
                    self.hand_counter += 1
                else:
                    self.hand_counter = 1
                # continue
            if play_more.lower() == 'n':
                print("Thanks for playing, Bye!")
                break

app = App()
app.run()