def position_to_move(row, col, matrix,command):
    if command == "up" and row - 1>=0:
        row-=1
    elif command == "down" and row+1 < len(matrix):
        row+=1
    elif command == "left" and col - 1>=0:
        col-=1
    elif command == "right" and col+1<len(matrix[row]):
        col+=1
    return row, col


def find_coals(i, j, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[j])):
            if matrix[i][j] == "c":
                return True
    else:
        return False


n = int(input())
commands = list(map(str, input().split(" ")))
matrix = [[str(j) for j in input().split()]for i in range(n)]
is_found = False
row = None
col = None
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "s":
            row = i
            col = j
            is_found = True
            break
    if is_found:
        break
count_coals =0
game_stop = False
for command in commands:
    row, col = position_to_move(row, col, matrix, command)
    if matrix[row][col] == "c":
        matrix[row][col] = "*"
        count_coals+=1
        if not find_coals(row, col, matrix):
            print(f"You collected all coals! ({row}, {col})")
            game_stop = True
            break
    elif matrix[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        game_stop = True
        break
remaining_coals = 0
if not game_stop:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]=="c":
                remaining_coals+=1
    print(f"{remaining_coals} coals left. ({row}, {col})")


