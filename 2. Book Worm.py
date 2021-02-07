def player_pos (matrix):
    for row in range (len (matrix)):
        for col in range (len (matrix[row])):
            if matrix[row][col] == 'P':
                return row, col


def movement(x,y, dx, dy):
    new_x = x+ dx
    new_y = y + dy
    if 0<=new_x <n and 0<=new_y<n:
        return new_x, new_y
    else:
        return x, y


string = input()
n = int(input())
matrix = [list(input()) for row in range(n)]
m = int(input())
dir = {'up':(-1, 0), 'down':(1, 0), 'left':(0,-1), 'right':(0,1)}
for _ in range(m):
    x, y = player_pos(matrix)
    commands = input()
    dx, dy = dir[commands]
    new_x, new_y = movement(x, y, dx, dy)
    if new_x == x and new_y == y:
        if len(string)>0:
            string = string[:-1]
    else:
        if not matrix[new_x][new_y] == '-':
            string+=matrix[new_x][new_y]
            matrix[new_x][new_y]='P'
            matrix[x][y] = '-'
        else:
            matrix[new_x][new_y] = 'P'
            matrix[x][y] = '-'
print(string)
for row in matrix:
    print("".join(row))