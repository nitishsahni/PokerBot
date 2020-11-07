from .table import *


class Player:
    """ The object that'll play the game. Each player can have a different strategy"""

    def __init__(self, money, table, strategy, big_blind=False, small_blind=False):
        self.money = money
        self.table = table
        self.strategy = strategy
        self.cards = []
        self.big_blind = big_blind
        self.small_blind = small_blind

    def check(self):
        return self.table.deep_copy(), self.deep_copy()

    def fold(self):
        new_player = self.deep_copy()
        new_table = self.table.deep_copy()
        new_table.still_in_game[0] = 0
        return new_table, new_player

    def call(self):
        new_player = self.deep_copy()
        new_player.money = self.money - self.table.to_call
        new_table = self.table.deep_copy()
        new_table.pot += self.table.to_call
        return new_table, new_player

    def raise_bet(self, amount):
        new_player = self.deep_copy()
        new_player.money = self.money - (self.table.to_call + amount)
        new_table = self.table.deep_copy()
        new_table.pot += self.table.to_call + amount
        return new_table, new_player

    def deep_copy(self):
        new_player = Player(self.money, self.table, self.strategy, self.big_blind, self.small_blind)
        new_player.cards = self.cards
        return new_player

    def make_move(self, move, table):
        if move[0] == 'fold' and table.to_call != 0:
            return self.fold()
        elif (move[0] == 'fold' and table.to_call == 0) or move[0] == 'check':
            return self.check()
        elif move[0] == 'call':
            return self.call()
        elif move[0] == 'raise':
            amt = move[1]
            return self.raise_bet(amt)
