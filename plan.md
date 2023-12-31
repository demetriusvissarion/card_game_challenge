## Phase One
General concepts of cards, players and hands:
* Cards (Card class and 52 instances thereof?) can be shuffled and dealt to 4 Player objects
* Concept of a "hand" is created for a Player, with some way to print that in an appropriate fashion to the terminal
## Phase Two
Ability to play cards, 13 "tricks" making a full round:
* Some user interaction such that the user can choose what card to play from their own hand
* "Bot" hands to play a card, chosen randomly for now (restrictions on who can play what, and who leads, to come later)
* Forming of "tricks" - 4 cards, 1 from each player - kept and preserved such that they can belong to a player who won that trick, later on
## Phase Three
Basic rules introduced:
* 2 Clubs owner goes first and plays that card first
* Players must follow suit, if possible
* Tricks are won by the player with the highest card of the leading suit (for now)
* Player who won the trick plays first card of next trick
## Phase Four
Full rules implemented:
* Scoring and calculation of tricks, including 1 point per Heart and 13 points for Q Spades
* Points are displayed in the terminal at round end
* (optionally, since it's absence won't take much away from the game) 3 cards are passed between players at the start of each round
* Hearts can only be played if no card matching the leading suit is playable - counts as "Hearts are broken"
* Hearts can only lead once broken, or if hand only has Hearts in it
* 26 points scored by everyone else if one player gets all Hearts and Q Spades
## Bonus
Begin adding some intelligent play to the "Bot" players e.g. (not necessarily in order):
* Try to avoid winning any tricks (players pass the 3 highest cards, and play only the lowest cards)
* Don't lead something like Q Spades or high Hearts if possible
* Throw away Q Spades if ever possible

Terms:
trick
hand
game


21/12/2023 To fix/add:
 - fix score per hand is too high, sum many times > 100, sum should be always 26
 - fix total_score does not reset between hands and ends up too big
 - add 'pass 3 cards' rule in app.py

22/12/2023 To fix/add:
 - fix show_hand error 
 AttributeError: 'list' object has no attribute 'name'

23/12/2023 To fix/add:
 - refactoring pass_three_cards hand 1 => not possible now, try again at the end
 - continue with pass_three_cards for hands 2,3,4
 - add "Hearts are broken" rule for user

24/12/2023 To fix/add:
 - add "Hearts are broken" rule for bots

25/12/2023 To fix/add:
 - add shooting_the_moon rule
 - add bot intelligent play
 - add throw 'Q♠' rules
 - fix "Last trick won by" that appears 7 times, should only appead once after last trick