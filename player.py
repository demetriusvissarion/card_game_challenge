class Player:
    def __init__(self, name):
        self.name = name
        # 'hand' list stores card objects
        self.hand = []
        self.score = 0