Card passing at start of the hand: (4 ways that repeat in order)
1. Hand 1: pass 3 cards to the opponent on your right: (the one before you, example player_2 passes to player_1)
2. Hand 2: pass 3 cards to the opponent on your left: (the one after you, example player_2 passes to player_3)
3. Hand 3: pass 3 cards to the opponent in front of you: (the one not after you or before you, example player_2 passes to player_4)
4. Hand 4: don't pass any cards
(these repeat for as many hands as th user plays)

First trick:
 - two of clubs starts of the hand
 - players cannot play a heart or the queen of spades

Broken hearts:
 - no one can start a trick (leading) with a heart until a heart was played in this hand

Calculate trick winner:
 - highest ranking card in the original suit wins the trick
 - trick winner starts the next trick (leading)
 - penalty cards in the trick (hearts or queen of spades) are added to the players penalty score

Calculate final score:
 - each heart gives one penalty point. 
 - the Queen of spades ('Q♠') gives 13 penalty points.

Winner of the Hand:
 - calcualted at end of hand (after trick 13, when all players hands are played)
 - the player with as few points as possible wins
 - if you get ALL penalty cards (13 hearts + Q♠) then you get 0 pts and all other players get 26 pts (Shooting the Moon!)

Score board:
 - populate it with player points after each hand
 - show score board as a table, with each hand on a row and totals at the bottom

Winner of the game:
 - when one or more players reach 100 points or more then the entire game is finished
 - the player with the least total points wins
 - if points > 100 and there are two or more equal with the least points then play continues until there's only one winner

Notes:
 * reset all variables at the end of a hand? => shouldn't be needed if I use a new instance of Hand class for each hand, and keep score in a different ScoreBoard class

21/12/2023 To fix:
 - score per hand is too high, sum many times > 100, sum should be always 26
 - 