def fibonacci():
    n1 = 0
    next_number = 1
    next_sum = 0
    while True:
        yield next_sum
        next_sum = n1 + next_number
        n1 = next_number
        if next_sum == 1:
            yield next_sum
        next_number = next_sum


generator = fibonacci()
for i in range(7):
    print(next(generator))




