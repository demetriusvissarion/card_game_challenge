from hand import Hand
from score_board import ScoreBoard

score_board = ScoreBoard()

# add here while loop to check if any players reached 100 score and if only one player has minimum score
while any(score_board.total_score[player] < 100 for player in score_board.total_score) and \
    sum(score_board.total_score[player] == min(score_board.total_score.values()) for player in score_board.total_score) > 1:
    new_hand = Hand()
    new_hand.start_hand()
    # save hand.score to the ScoreBoard class
    score_board.hands_score.append(new_hand.score)
    print(f'Hand won by {new_hand.hand_winner}')
    score_board.score_table()

    print('Do you want to play another hand? (y/n)')

    # exception handling and validation
    while True:
        try:
            play_more = input("Your selection: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... return to the start of the loop
            continue
        if play_more in ['y', 'Y', 'n', 'N']:
            if play_more in ['y', 'Y']:
                print("Ok, starting another hand")
                break
            else:
                #we're ready to exit the loop.
                print("Thanks for playing, Bye!")
                break

    if play_more.lower() == 'y':
        print('Get ready')
        continue
    if play_more.lower() == 'n':
        print('Get ready')
        break



# ### Test data
# test_hand1 = Hand()
# test_hand2 = Hand()
# # Create some hands and add them to the ScoreBoard
# test_hand1.score = {'Player_1': 10, 'Player_2': 2, 'Player_3': 0, 'Player_4': 14}
# test_hand2.score = {'Player_1': 6, 'Player_2': 13, 'Player_3': 4, 'Player_4': 3}
# score_board.hands_score.extend([test_hand1, test_hand2])

# # Print the score table
# score_board.score_table()