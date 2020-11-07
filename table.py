class Table:

    def __init__(self, big_blind, small_blind, players=2):
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.pot = big_blind + small_blind
        self.players = players
        self.to_call = 0
        self.flop = None
        self.turn = None
        self.river = None
        self.still_in_game = [1] * players

    def update(self):
        """changed pot, number of players in total, to_call for my player, and the players who haven't folded."""
        return "players cards"

    def deep_copy(self):
        new_table = Table(self.big_blind, self.small_blind, self.players)
        new_table.to_call = self.to_call
        new_table.flop, new_table.turn, new_table.river = self.flop, self.turn, self.river
        new_table.still_in_game = self.still_in_game
        return new_table
