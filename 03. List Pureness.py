from collections import deque


def best_list_pureness(*test):
    numbers = deque(map(int, test[0]))
    k = test[1]
    pureness = 0
    rotation = 0
    for r in range(k+1):
        current_pureness = 0
        for i in range(len(numbers)):
            current_pureness+=numbers[i]*i
        if current_pureness > pureness:
            pureness = current_pureness
            rotation = r
        current_digit = numbers.pop()
        numbers.appendleft(current_digit)

    return f'Best pureness {pureness} after {rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

