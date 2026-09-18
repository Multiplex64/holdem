import random

class game:
    def __init__(self, players = [], buy_in = 5):
        self.players = players
        self.buy_in = buy_in

    def add_player(self, player):
        self.players.append(player)
        player.game = self

    def remove_player(self, player):
        self.players.remove(player)
        player.game = None


class player:
    def __init__(self, name = 'player', chips = 100):
        self.name = name
        self.chips = chips
        self.game = None

    def join_game(self, game):
        game.add_player(self)

    def leave_game(self, game):
        game.remove_player(self)