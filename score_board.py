class ScoreBoard:
    def __init__(self):
        self.hands_score = []
        # Initialize a dictionary to store the total score for each player
        self.total_score = {f'Player_{i}': 0 for i in range(1, 5)}

    def score_table(self):
        # Print the header row with horizontal lines
        print(f"{'=' * 50}")
        print(f"{'Hand':<10}|{'Player_1':<10}|{'Player_2':<10}|{'Player_3':<10}|{'Player_4':<10}|")
        print(f"{'=' * 50}")

        for i, hand in enumerate(self.hands_score, start=1):
            # Print the scores for each player in the current hand with vertical lines
            print(f"{i:<10}|{hand.score['Player_1']:<10}|{hand.score['Player_2']:<10}|{hand.score['Player_3']:<10}|{hand.score['Player_4']:<10}|")
            print(f"{'-' * 50}")

            # Update the total score for each player
            for player in self.total_score:
                self.total_score[player] += hand.score[player]

        # Print the total score row with horizontal lines
        print(f"{'Total Score':<10}|{self.total_score['Player_1']:<10}|{self.total_score['Player_2']:<10}|{self.total_score['Player_3']:<10}|{self.total_score['Player_4']:<10}|")
        print(f"{'=' * 50}")
