# FinalProject
## Blackjack Game
# This is a Python implementation of the popular card game Blackjack. The project consists of multiple files that handle different aspects of the game, including the deck of cards, player's hand, probability calculations, and the game logic.

# Files
# The project is organized into the following files:

# deck.py: This file contains the Deck class, which represents a deck of playing cards. It provides methods for shuffling the deck, drawing a card, and calculating the probability of drawing a specific card.

# hand.py: The Hand class in this file represents a player's or dealer's hand of cards. It handles actions such as initializing the hand, calculating the total value of the hand, checking for a blackjack or bust, and allowing the player to hit (draw a new card).

# probability.py: This file contains the ProbabilityCalculator class, which provides methods for calculating probabilities in the game. It includes functions to calculate the win probability based on player and dealer values, as well as the probability of drawing a specific card from the deck.

# game_prob.py: This is the main file that runs the blackjack game. It initializes the deck, plays the game by managing player and dealer hands, calculates win probabilities, and determines the game outcome. It also allows the player to choose Hit or Stand actions and handles the dealer's actions.

# Running the Game
# To play the game, run the game_prob.py file. It will start a new game of blackjack. Follow the prompts to make decisions during the game, such as hitting or standing. The game will display the hands, probabilities, and outcomes.

# Game Rules
# The blackjack game follows standard rules:

# The goal is to obtain a hand with a total value closer to 21 than the dealer's hand, without exceeding 21 (bust).
# Numbered cards (2-10) have their face values, face cards (J, Q, K) are worth 10, and an Ace (A) can be counted as 1 or 11.
# A blackjack is achieved with an Ace and a 10-point card (J, Q, K) in the initial two-card hand.
# Players can choose to Hit (draw a new card) or Stand (end their turn) during their round.
# The dealer hits until their hand value reaches 17 or more.
# If a player busts (exceeds 21), they lose the game. If the dealer busts, the player wins. If neither busts, the hand with a higher value wins. A tie results in a push.
##
