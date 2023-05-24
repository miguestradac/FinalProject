from deck import Deck
from hand import Hand
from probability import ProbabilityCalculator


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        player = Hand(self.deck)
        dealer = Hand(self.deck, is_dealer=True)

        # Show probabilities after initial draw
        for card in set(player.cards):
            prob = ProbabilityCalculator.card_probability(self.deck, card)
            print(f"Probability of drawing {card}: {prob * 100}%")

        # Players' actions
        while not player.blackjack() and not player.is_busted():
            print(f"Your hand: {player.cards} Total: {player.total_value()}")
            print(f"Dealer's first card: {dealer.cards[0]}")
            action = input("Do you want to Hit or Stand? (H/S): ")
            if action.lower() == 'h':
                player.hit()
            else:
                break

        # Dealers' actions
        while dealer.total_value() < 17:
            dealer.hit()

        # Game results
        print(f"Your hand: {player.cards} Total: {player.total_value()}")

        if player.is_busted():
            print("You busted! Dealer wins.")
        else:
            print(f"Dealer's hand: {dealer.cards} Total: {dealer.total_value()}")

            if dealer.is_busted():
                print("Dealer busted! You win.")
            elif player.cards == ['A', 'J'] or player.cards == ['A', 'Q'] or player.cards == ['A', 'K']:
                print("You have a blackjack! You win.")
            elif dealer.cards == ['A', 'J'] or dealer.cards == ['A', 'Q'] or dealer.cards == ['A', 'K']:
                print("Dealer has a blackjack! Dealer wins.")
            elif player.total_value() > dealer.total_value():
                print("You win!")
            elif player.total_value() < dealer.total_value():
                print("Dealer wins!")
            else:
                print("It's a tie!")

        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.lower() == 'y':
            self.play()
        else:
            print("Thanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.play()
