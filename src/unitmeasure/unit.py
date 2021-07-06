class Unit(object):

    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        if not isinstance(other, Unit):
            return False

        return self.symbol == other.symbol