# Optiver Coingame
This is a python simulation of the Optiver Coin Game that they made me play in the final round of their trading interview.

This game was recreated from memory to be as similar as possible to the game that was presented to me.

## Author: Prithvi P Rao

# Game Structure
The game involves 5 players, you and 4 bots, bidding on the outcome of a coin flip. The returns of the game is based on this rule: The total money bid on the wrong outcome is divided amongst the people who bid on the right outcome in the ratio of their bids.

## Observations:

1. Negative Sum Game : There is a 1/32 chance all player bet on one face and the coin lands on the other. In this case, all money that was bid is lost and thus the game is a Negative Sum game and not a Zero Sum Game.

2. Player Patterns: Player Number 4 always bids the same amount and on Heads every time. Player number 2 bids a regular amount which varies around 50 and the choice of outcome is always the opposite of the previous outcome. 

## Strategical Conclusions:

1. Bidding on heads is a safe strategy, you are always splitting your losses and wins with Player number 4. 

2. When the previous outcome is a Tail, bidding on heads will be a poor decision, as you have a 50% chance you lose all your money and in the rare case you guess the right ourcome, you will be splitting your reward with 2 others(minimum).
