class Card:
    def __init__(self, number, suit, name=None):
        self.number = number
        self.suit = suit
        self.name = name or f'{number}{suit}'