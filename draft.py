

cards = ['A♦', 'Q♣', '7♣', 'A♥', 'K♥', '7♥', '8♥', 'J♥', '5♠', '9♠', '10♠', 'A♠', '3♦', '5♦', '3♣', '4♣', '8♣', '10♣']

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def lowest_card(card_list):
    lowest_card = card_list[0]

    for card in card_list[1:]:
        if card_values[card[:-1]] < card_values[lowest_card[:-1]]:
            lowest_card = card

    return lowest_card


result = lowest_card(cards)
print(f"The lowest card is: {result}")






