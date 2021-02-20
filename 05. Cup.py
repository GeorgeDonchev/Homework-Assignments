class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.space = int

    def fill(self, milliliters):
        if milliliters + self.quantity<=self.quantity:
            self.space = self.quantity - (milliliters + self.quantit)
        return self.space

    def status(self):
        return self.space()


cup = Cup(100, 50)
# cup.fill(10)
cup.fill(10)
print(cup.status())
