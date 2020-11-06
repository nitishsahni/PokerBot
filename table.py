
class Table:

    def __init__(self, big_blind, small_blind, players=2):
        self.pot = big_blind + small_blind
        self.players = players
        self.to_call = 0
        self.still_in_game = [1] * players

    def update(self):
        """changed pot, number of players in total, to_call for my player, and the players who haven't folded."""
        return "players cards"
