## Phase One
General concepts of cards, players and hands:
* Cards (Card class and 52 instances thereof?) can be shuffled and dealt to 4 Player objects
* Concept of a "hand" is created for a Player, with some way to print that in an appropriate fashion to the terminal
# notes: 
# - generates an instance of each card
# - allows cards to be shuffled
# - allows cards to be dealt to 4 players (remember which cards where played)
# Concept of a "hand" is created for a Player
# The "hand" can be printed to the terminal (create a show_hand() function within the class ???)

## Phase Two
Ability to play cards, 13 "tricks" making a full round:
* Some user interaction such that the user can choose what card to play from their own hand
* "Bot" hands to play a card, chosen randomly for now (restrictions on who can play what, and who leads, to come later)
* Forming of "tricks" - 4 cards, 1 from each player - kept and preserved such that they can belong to a player who won that trick, later on
# notes: 
# - ability to play cards: 13 "tricks" (rounds) => so deal 13 cards/player at start
# - user can choose what card to play from their own hand => remove chosen card from hand
# - bot payed cards chosen randomly
# - forming of "tricks" - 4 cards, 1 from each player
# - decide each "trick" winner and save the cards to his stack 

## Phase Three
Basic rules introduced:
* 2 Clubs owner goes first and plays that card first
* Players must follow suit, if possible
* Tricks are won by the player with the highest card of the leading suit (for now)
* Player who won the trick plays first card of next trick
# notes: 
# - 2 Clubs owner goes first and plays that card first
# - players must follow suit
# - tricks are won by the player with the highest card of the leading suit
# - player who won the trick plays first card of next trick

## Phase Four
Full rules implemented:
* Hearts can only be played if no card matching the leading suit is playable - counts as "Hearts are broken"
* Hearts can only lead once broken, or if hand only has Hearts in it
* Scoring and calculation of tricks, including 1 point per Heart and 13 points for Q Spades
* 26 points scored by everyone else if one player gets all Hearts and Q Spades
* Points are displayed in the terminal at round end
* (optionally, since it's absence won't take much away from the game) 3 cards are passed between players at the start of each round

## Bonus
Begin adding some intelligent play to the "Bot" players e.g. (not necessarily in order):
* Try to avoid winning any tricks
* Throw away Q Spades if ever possible
* Don't lead something like Q Spades or high Hearts if possible


