# Imports
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
    pass

  # the flop
  def round_flop(self):
    pass

  # the turn
  def round_turn(self):
    pass

  # the river
  def round_river(self):
    pass

  # the showdown
  def round_showdown(self):
    pass


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


if __name__ == "__main__":
  shell_game()
