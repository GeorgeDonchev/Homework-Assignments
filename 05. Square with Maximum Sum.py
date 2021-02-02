def read_matrix():
    rows, cols = map (int, input ().split (", "))
    matrix = [list (map (int, input ().split (", "))) for x in range (rows)]
    return matrix


matrix = read_matrix ()
biggest_sum = None
current_sum = 0
best_start = None
for index in range (len (matrix)-1):
    row = matrix[index]
    for j in range(len(row)-1):
        current_sum = matrix[index][j] + matrix[index][j + 1] + matrix[index + 1][j] + matrix[index+1][j+1]

        if biggest_sum is None or current_sum > biggest_sum:
            biggest_sum = current_sum
            best_start = (index, j)

rows, cols = best_start
for row in range(rows, rows+2):
    for col in range(cols, cols+2):
        print(matrix[row][col], end = " ")
    print()
print(biggest_sum)

