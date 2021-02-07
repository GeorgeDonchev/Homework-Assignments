def find_the_end(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "B":
                return row, col


snake_pos = tuple()
n = int(input())
territory = [list(input())for i in range(n)]
for i in range(n):
    for j in range(len(territory[i])):
        if territory[i][j] == "S":
            snake_pos = (i, j)
            break

food_count = 0
game_over = False

movement = {"up": (-1, 0), "down": (1, 0), "left": (0,-1), "right":(0,1)}
while not game_over:
    command = input()
    x, y = snake_pos
    territory[x][y] = "."
    dx, dy = movement[command]
    new_x = dx + x
    new_y = dy + y
    if new_x < 0 or new_x >= len(territory) or new_y < 0 or new_y >= len(territory[new_x]):
        game_over = True
        break
    if territory[new_x][new_y] == "*":
        food_count += 1
    elif territory[new_x][new_y] == "B":
        territory[new_x][new_y]= "."
        new_x, new_y = find_the_end(territory)
    territory[new_x][new_y] = "S"
    if food_count>=10:
        game_over = True
        break

    snake_pos = new_x, new_y

if food_count>=10:
    print('You won! You fed the snake.')
else:
    print("Game over!")
print(f"Food eaten: {food_count}")
for row in range(n):
    for col in range(len(territory[row])):
        print(territory[row][col], end = "")
    print()