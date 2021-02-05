def multiply(*args):
    res = 1
    for digit in args:
        res*=digit
    return res


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
