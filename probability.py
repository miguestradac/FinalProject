class ProbabilityCalculator:
    @staticmethod
    def win_probability(player_value, dealer_card_value):
        if player_value > dealer_card_value:
            return 1
        elif player_value == dealer_card_value:
            return 0.5
        else:
            return 0

    @staticmethod
    def card_probability(deck, card):
        return deck.card_probability(card)
