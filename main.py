# Imports
import random

card_ranks = [
    "Ace",
    "King",
    "Queen",
    "Jack",
    "Ten",
    "Nine",
    "Eight",
    "Seven",
    "Six",
    "Five",
    "Four",
    "Three",
    "Two",
]

card_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

total_cards = [(x, y) for x in card_ranks for y in card_suits]
print(total_cards)

"""
Class for poker hands
"""


class hand:
    def __init__(self, cards=[]):
        self.cards = cards


"""
Class for game objects
"""


class game:
    # init class
    def __init__(self, players=[], buy_in=5):
        self.players = players
        self.buy_in = buy_in
        self.pot = 0
        self.deck = total_cards
        random.shuffle(self.deck)

    # add a player object to the game
    def add_player(self, player):
        self.players.append(player)
        player.game = self

    # remove a player from the game
    def remove_player(self, player):
        self.players.remove(player)
        player.game = None


"""
Class for player objects
"""


class player:
    # init class
    def __init__(self, name="player", chips=100):
        self.name = name
        self.chips = chips
        self.game = None

    # add player to a game object
    def join_game(self, game):
        game.add_player(self)

    # exit from a game object
    def leave_game(self, game):
        game.remove_player(self)


"""
Shell-based game
"""


def shell_game():
    g = game()
    print(g.deck)


if __name__ == "__main__":
    shell_game()
