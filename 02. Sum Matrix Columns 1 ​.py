def read_matrix():
    rows, cols = map(int, input().split(", "))
    matrix = [list(map(int, input().split())) for row in range(rows)]
    return matrix

matrix = read_matrix()
current_cal =0
i = 0
row = 0
sum_col =0
for col in range(len(matrix[row])):
    for row in range(len(matrix)):
        sum_col+=matrix[row][col]
    print(sum_col)
    sum_col = 0