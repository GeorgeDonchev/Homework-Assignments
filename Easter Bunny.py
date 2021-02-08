import sys


def is_valid (value,size):
    if 0<=value<size:
        return True


n = int(input())
matrix = [[j for j in input().split()]for i in range(n)]
print(matrix)
bunny_pos = ()
directions = {"up":(-1,0), "right":(0, 1), "down":(1, 0), "left":(0, -1)}
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == "B":
            bunny_pos = (r, c)

best_sum = - sys.maxsize
best_directioin = ''
for direction in directions:
    row = bunny_pos[0]
    col = bunny_pos[1]
    current_sum = 0
    row_changes = directions[direction][0]
    col_changes = directions[direction][1]
    if not is_valid(row+row_changes, n) and not is_valid(col+col_changes, n):
        continue

    while is_valid(row, n) and is_valid(col, n):
        current_cell = matrix[row][col]
        if current_cell != "B" and current_cell != "x":
            current_sum+=int(current_cell)
        elif current_cell == "x":
            break
        row += directions[direction][0]
        col += directions[direction][1]
    if current_sum and current_sum > best_sum:
        best_sum = current_sum
        best_directioin = direction

print(best_directioin)
row = bunny_pos[0] + directions[best_directioin][0]
col = bunny_pos[1]+ directions[best_directioin][1]
while is_valid(row, n) and is_valid(col, n):
    if matrix[row][col]=="x":
        break
    print([row, col])
    row +=directions[best_directioin][0]
    col+=directions[best_directioin][1]
print(best_sum)