# OA 1 for Akuna Capital, Chicago, HackerRank Test 1
___
## Coding 1
### Descriptiong
Miriam and Alejandro are playing a card game with a deck of custom cards, each of which contains a single number of it, with numbers possibly duplicated across multiple cards and negative numbers allowed. To begin the game, the first player draws the top card from the deck and adds its face value to their score. If the value of the card is a multiple of 3 , then the deck is flipped, such that the second player draws a card from what was previously the bottom of the deck; if the value is not a multiple of 3, the deck stays in its current orientation. This continues back-and-forth until all cards have been drawn, at which point the player with the highest score wins. Note that the deck may not initially have an even number of cards, so it is possible for the first player to draw one card more than the second player over the course of the game. It is also possible for the players to draw/tie.

### Problem Statement

Assume that Miriam always draws the first card. Implenyent the following function in the code editor to compute the difference between Miriam's score and Âlejandro's score at the conclusion of the game.
```C++
/// @param deck The initial ordered sequence of card face values in the game's deck
/// @pre @p deck is not empty
/// @returns The difference between Miriam's and Alejandro's scores at the end of the game, assuming that Miriam draws
/// the first card. A positive return value indicates that Miriam won the game, while a negative return value
/// indicates that Alejandro won the game. A return value of θ indicates a draw/tie. 
int computeDifference (const std::vector <int>&deck)
```

### Example
Consider a game in which the deck initially contains 5 cards whose face values are the sequence $[3,7, 2,6,5]$. Let's assume, as the problem states, that Miriam draws first:
+ **0^th^ Round** - The score begins Miriam 0 vs. Alejandro.
+ **1^st^ Round** - Miriam draws the top card, which has value 3. The score is now Miriam 3 vs Alejandro 0 , and the deck is flipped because 3 is a multiple of 3 . The remaining cards are now $[5,6,2,7]$.
+ **2^nd^ Round** - Alejandro draws the top card, which has value 5. The score is now Miriam 3 vs. Alejandro 5, and the deck remains in its current orientation because 5 is not a multiple of 3. The remaining cards are now $[6,2,7]$.
+ **3^rd^ Round** - Miriam draws the top card, which has value 6. The score is now Miriam 9 vs. Alejandro 5 , and the deck is flipped because 6 is a multiple of 3 . The remaining cards are now [7,2]. 
+ **4^th^ Round** - Alejandro draws the top card, which has value 7. The score is now Miriam 9 vs. Alejandro 12, and the deck remains in its current orientation because 7 is not a multiple of 3. The remaining cards are now [2].
+ **5^th^ Round** - Miriam draws the top card, which has value 2. The score is now Miriam 11 vs. Alejandro 12 , and the deck is empty: the game is over.
  
 The function should therefore return -1.
 
 
### Test Case Format

| STDIN |         | FUNCTION              |
| ----- | ------- | --------------------- |
| 5     | &#8594; | deck.size() == 5      |
| 3     | &#8594; | deck == { 3,7,2,6,5 } |
| 7     |         |                       |
| 2     |         |                       |
| 6     |         |                       |
| 5     |         |                       |


___
\&#8594; is the right arrow in mark down.

