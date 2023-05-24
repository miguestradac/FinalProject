import random
from collections import Counter


class Deck:
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']*4

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def card_probability(self, card):
        card_counts = Counter(self.cards)
        return card_counts[card] / len(self.cards) if len(self.cards) > 0 else 0
