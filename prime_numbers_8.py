import math


def get_primes(numbers):
    for number in numbers:
        if number == 2:
            yield number

        elif number > 1:
            current_num = int(math.sqrt(number))
            count = 0
            for i in range(2, current_num+1):
                if number % i == 0:
                    count+=1
            if count == 0:
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 11, 13, 37, 41])))

