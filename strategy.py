class Strategy:
    """Template strategy"""

    def __init__(self):
        pass

    def think(self, player):
        pass


class AlwaysFold(Strategy):

    def think(self, player):
        return "fold"
