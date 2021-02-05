import itertools
numbers = [num for num in input().split(", ")]
n = len(numbers)
permutations = set(itertools.permutations(["-"]*n + ["+"]*n, n))

for permutation in permutations:
    expresion = "".join(itertools.chain(*zip(permutation, numbers)))
    res = eval(expresion)
    print(f"{expresion}={res}")
