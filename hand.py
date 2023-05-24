from collections import Counter


class Hand:
    def __init__(self, deck, is_dealer=False):
        self.deck = deck
        self.is_dealer = is_dealer
        self.cards = [deck.draw_card(), deck.draw_card()]

    def card_value(self, card):
        if card in ('J', 'Q', 'K'):
            return 10
        elif card == 'A':
            return 11  # Initially treat 'A' as 11
        else:
            return int(card)

    def total_value(self):
        value = sum(self.card_value(card) for card in self.cards)
        # If value > 21 and 'A' is in hand, treat 'A' as 1
        if value > 21 and 'A' in self.cards:
            counts = Counter(self.cards)
            for _ in range(counts['A']):
                value -= 10  # reduce 'A's value to 1
                if value <= 21:
                    break
        return value

    def blackjack(self):
        return self.total_value() == 21 and len(self.cards) == 2

    def is_busted(self):
        return self.total_value() > 21

    def hit(self):
        self.cards.append(self.deck.draw_card())
