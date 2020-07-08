class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, dollars, cents):
        if self.cents + cents >= 100:
            self.dollars = self.dollars + dollars + ((self.cents + cents) // 100)
            self.cents = (self.cents + cents) % 100
        else:
            self.dollars = self.dollars + dollars
            self.cents = self.cents + cents
