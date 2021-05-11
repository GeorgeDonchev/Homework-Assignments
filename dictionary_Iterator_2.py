class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.length = len(self.dictionary)
        self.keys = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.length:
            temp = self.counter
            self.counter+=1
            return (self.keys[temp], self.values[temp])
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


