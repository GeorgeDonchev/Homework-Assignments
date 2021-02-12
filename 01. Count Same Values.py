inputs = tuple (map (float, input ().split ()))
sequences = {}

for element in inputs:
    if element not in sequences:
        sequences[element] = 0
    sequences[element] += 1

for key, value in sequences.items():
    print(f'{key} - {value} times')