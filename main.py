# Imports
import os
import random

# ranks
card_ranks = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

# suits
card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# List of all cards arranged by value
total_cards = {
    card_ranks[x] + " of " + card_suits[y]: (x, y, card_ranks[x], card_suits[y])
    for x in range(len(card_ranks))
    for y in range(len(card_suits))
}

global_players = []


"""
Clear the Python Terminal
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


"""
Class for poker hands
"""


class hand:
    def __init__(self, cards=[]):
        self.cards = cards

    def calculate(self):
        pass


"""
Class for game objects
"""


class game:
    # init class
    def __init__(self, players=[], buy_in=5):
        self.players = players
        self.buy_in = buy_in
        self.pot = 0
        self.board = []
        deck = list(total_cards.items())
        random.shuffle(deck)
        self.deck = dict(deck)

    # add a player object to the game
    def add_player(self, player):
        self.players.append(player)
        player.game = self

    # remove a player from the game
    def remove_player(self, player):
        self.players.remove(player)
        player.game = None

    # pre-flop
    def round_preflop(self):
        for p in self.players:
            p.cards = [self.deck.popitem(), self.deck.popitem()]

    # the flop
    def round_flop(self):
        for _ in range(3):
            self.board.append(self.deck.pop())

    # the turn
    def round_turn(self):
        self.board.append(self.deck.pop())

    # the river
    def round_river(self):
        self.board.append(self.deck.pop())

    # the showdown
    def round_showdown(self):
        pass


"""
Class for player objects
"""


class player:
    # init class
    def __init__(self, name="", chips=100):
        if len(name) > 0:
            self.name = name
        else:
            self.name = "Player" + str(random.randint(0, 9999)).rjust(4, "0")
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

    def ask_bet():
        input("F: Fold | M: Match | B: Bet | A: All-In")

    players = []
    clear()
    print("\nWelcome to Texas Hold'em.")
    while True:
        while True:
            user_input = input(
                "\nA: Add Player | R: Remove Player | S: Start Game | X: Exit\n>> "
            )
            match user_input.lower():
                case "x":
                    return
                case "s":
                    if len(players) >= 2:
                        break
                    else:
                        print("You Need At Least 2 Players to Start.")
                case "a":
                    p = player(input("\nEnter Player Name \n>> "))
                    players.append(p)
                    print(
                        "Congratulations "
                        + p.name
                        + ", You Have Joined the Game. You Start With",
                        p.chips,
                        "Chips.",
                    )
                case "r":
                    pass
        # start the game
        print("\nStarting Game...")
        print("\nPlayers:")
        for p in players:
            print(p.name)
        input("Press Enter to Begin.\n")
        clear()
        g = game(players)

        # preflop
        g.round_preflop()
        for p in players:
            input(p.name + ": Press Enter to See Your Cards.")
            print("Your Cards:")
            for card in p.cards:
                print(card[0])
            input("Press Enter to Continue.")
            clear()


if __name__ == "__main__":
    shell_game()
