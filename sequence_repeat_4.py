class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0
        self.length = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.idx
        if self.idx < self.number:
            self.idx +=1
            return self.sequence[temp % self.length]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
