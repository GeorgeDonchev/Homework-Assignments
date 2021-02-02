def read_matrix():
    rows, cols = tuple(map(int, input().split()))
    matrix = [[int(j) for j in input().split()] for i in range(rows)]
    return matrix


matrix = read_matrix()
max_sum = None
best_start = None

for i in range(len(matrix)-2):
    current_sum = 0
    current_matrix = []
    row_count = i
    for j in range(len(matrix[i])-2):
        col_count = j
        current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if max_sum is None or current_sum > max_sum:
            max_sum = current_sum
            best_start = (i,j)
(i, j) = best_start
print(f"Sum = {max_sum}")
for row in range(i, i+3):
    for col in range(j, j+3):
        print(matrix[row][col], end = " ")
        # print(col, end = " ")
    print()