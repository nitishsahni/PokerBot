class Player:

    """ The object that'll play the game. Each player can have a different strategy"""

    def __init__(self, money, table, strategy, big_blind=False, small_blind=False):
        self.money = money
        self.table = table
        self.strategy = strategy
        self.cards = []
        self.big_blind = big_blind
        self.small_blind = small_blind

    def get_table(self):
        self.cards = self.table.update()
        return self.table

    def check(self):
        pass

    def fold(self):
        pass

    def call(self):
        pass

    def raise_bet(self, amount):
        pass

    def make_move(self):
        table = self.get_table()
        move = self.strategy.think(table, self)
        if move[0] == 'fold' and table.to_call != 0:
            return self.fold()
        elif (move[0] == 'fold' and table.to_call == 0) or move[0] == 'check':
            return self.check()
        elif move[0] == 'call':
            return self.call()
        elif move[0] == 'raise':
            amt = move[1]
            return self.raise_bet(amt)




