from functools import reduce


def operate(op,*args):
    if op == '+':
        return reduce(lambda a, b: a+b, args)
    elif op == '-':
        return reduce(lambda a, b: a-b, args)
    elif op == "*":
        return reduce(lambda a, b: a*b, args)
    elif op =='/':
        return reduce(lambda a, b: a/b, args)


print(operate("/", 1, 2, 3))