class ScoreBoard:
    def __init__(self):
        self.hands_score = []
        # Initialize a dictionary to store the total score for each player
        self.total_score = {'Player_1': 0, 'Player_2': 0, 'Player_3': 0, 'Player_4': 0}

    def reset_total_score(self):
        self.total_score = {'Player_1': 0, 'Player_2': 0, 'Player_3': 0, 'Player_4': 0}

    def score_table(self):
        self.reset_total_score()
        # Print the header row with horizontal lines
        print(f"{'=' * 58}")
        print(f"{'Hand':<13}|{'Player_1':<10}|{'Player_2':<10}|{'Player_3':<10}|{'Player_4':<10}|")
        print(f"{'=' * 58}")

        for i, hand in enumerate(self.hands_score, start=1):
            # Print the scores for each player in the current hand with vertical lines
            print(f"{i:<13}|{hand['Player_1']:<10}|{hand['Player_2']:<10}|{hand['Player_3']:<10}|{hand['Player_4']:<10}|")
            print(f"{'-' * 58}")

            # Update the total score for each player
            for player in self.total_score:
                self.total_score[player] += hand[player]

        # Print the total score row with horizontal lines
        print(f"{'Total Score':<13}|{self.total_score['Player_1']:<10}|{self.total_score['Player_2']:<10}|{self.total_score['Player_3']:<10}|{self.total_score['Player_4']:<10}|")
        print(f"{'=' * 58}")
