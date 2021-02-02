def possitions_to_move(i, j, matrix, command):
    if command == "U":
        i-=1
    elif command == "D":
        i+=1
    elif command == "L":
        j-=1
    elif command == "R":
        j+=1
    return i,j


rows, cols = tuple(map(int, input().split()))
matrix = [[str(j) for j in input()]for i in range(rows)]
commands = input()
is_killed = False
is_escaped = False
for command in commands:
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "B":
                i, j = possitions_to_move(row, col, matrix, command)
                if 0>i or i>=len(matrix) or 0>j or j>=len(matrix):
                    continue
                if matrix[i][j] == "P":
                    is_killed = True
                    break
                matrix[i][j] = "B"
            elif matrix[row][col] == "P":
                i, j = possitions_to_move (row, col, matrix, command)
                if matrix[i][j] == "B":
                    is_killed = True
                    break
                elif 0>i or i>=len(matrix) or 0>j or j>=len(matrix[i]):
                    is_escaped = True
                    break
                else:
                    matrix[row][col]="."
                    matrix[i][j]="P"
        if is_killed or is_escaped:
            break
    if is_killed:
        print(f"dead: {i} {j}")
        break
    elif is_escaped:
        print(f"won: {i} {j}")

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end = " ")
    print()