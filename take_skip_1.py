class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.var = -step

    def __iter__(self):
        return self

    def __next__(self):
        self.var += self.step
        if self.count > 0:
            self.count-=1
            return self.var
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

