from collections import deque
rows, cols = tuple(map(int, input().split()))
matrix = [ [None for n in range(cols)] for i in range(rows)]

snake =deque(list(input()))

for row in range(rows):
    temp = ""
    for col in range(cols):
        symbol = snake.popleft()
        temp+=symbol
        snake.append(symbol)
    if row % 2 == 0:
        print(temp)
    else:
        print(temp[::-1])



