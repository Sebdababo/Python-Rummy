import random
import itertools

class Card:
    SUIT_SYMBOLS = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}
    RANK_ORDER = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.abbr = self.get_abbreviation()

    def get_abbreviation(self):
        rank_abbr = self.rank[0] if self.rank != '10' else '10'
        return f"{rank_abbr}{self.SUIT_SYMBOLS[self.suit]}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if self.suit != other.suit:
            return list(self.SUIT_SYMBOLS.keys()).index(self.suit) < list(self.SUIT_SYMBOLS.keys()).index(other.suit)
        return self.RANK_ORDER[self.rank[0] if self.rank != '10' else '10'] < self.RANK_ORDER[other.rank[0] if other.rank != '10' else '10']

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        self.hand.append(card)
        self.sort_hand()

    def discard(self, card):
        self.hand.remove(card)

    def sort_hand(self):
        self.hand.sort()

class RummyGame:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.discard_pile = []

    def deal_initial_hands(self):
        for _ in range(7):
            for player in self.players:
                player.draw(self.deck.draw())
        self.discard_pile.append(self.deck.draw())

    def is_valid_meld(self, cards):
        if len(cards) < 3:
            return False
        
        # Check for set
        if all(card.rank == cards[0].rank for card in cards):
            return True
        
        # Check for run
        if all(card.suit == cards[0].suit for card in cards):
            ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
            card_ranks = [ranks.index(card.rank) for card in cards]
            card_ranks.sort()
            return all(card_ranks[i] == card_ranks[i-1] + 1 for i in range(1, len(card_ranks)))

        return False

    def get_input(self, prompt):
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            print("Game stopped. Thanks for playing!")
            exit()
        return user_input

    def play_turn(self, player):
        print(f"\n{player.name}'s turn:")
        print("Your hand:", " ".join(card.abbr for card in player.hand))
        print("Top of discard pile:", self.discard_pile[-1].abbr if self.discard_pile else "Empty")
        
        # Player draws a card
        while True:
            draw_from = self.get_input("Draw from deck (d) or discard pile (p): ").lower()
            if draw_from in ['d', 'p']:
                break
            print("Invalid input. Please try again.")
        
        if draw_from == 'p' and self.discard_pile:
            card = self.discard_pile.pop()
            print(f"You drew {card.abbr} from the discard pile.")
        else:
            if draw_from == 'p' and not self.discard_pile:
                print("Discard pile is empty. Drawing from deck instead.")
            card = self.deck.draw()
            print(f"You drew {card.abbr} from the deck.")
        player.draw(card)
        
        # Player discards a card
        print("Your hand:", " ".join(card.abbr for card in player.hand))
        while True:
            discard_input = self.get_input("Enter the abbreviation of the card to discard: ")
            matching_cards = [card for card in player.hand if card.abbr == discard_input]
            if matching_cards:
                discard = matching_cards[0]
                break
            print("Invalid input. Please enter a valid card abbreviation from your hand.")
        
        player.discard(discard)
        self.discard_pile.append(discard)
        print(f"You discarded {discard.abbr}")

    def check_winner(self, player):
        # Check if all cards form valid melds
        temp_hand = player.hand.copy()
        while temp_hand:
            found_meld = False
            for i in range(3, len(temp_hand) + 1):
                for meld in itertools.combinations(temp_hand, i):
                    if self.is_valid_meld(meld):
                        for card in meld:
                            temp_hand.remove(card)
                        found_meld = True
                        break
                if found_meld:
                    break
            if not found_meld:
                return False
        return True

    def play_game(self):
        self.deal_initial_hands()
        current_player = 0

        while True:
            player = self.players[current_player]
            self.play_turn(player)

            if self.check_winner(player):
                print(f"\n{player.name} wins!")
                break

            current_player = (current_player + 1) % len(self.players)

        print("Game over. Thanks for playing!")

if __name__ == "__main__":
    game = RummyGame()
    game.play_game()