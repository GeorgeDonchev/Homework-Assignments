from itertools import permutations


def possible_permutations(numbers):
    possibilities = permutations(numbers)
    for couples in list(possibilities):
        yield list(couples)


[print(n) for n in possible_permutations([1, 2, 3])]