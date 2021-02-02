def read_matrix ():
    rows, cols = tuple(map(int, input().split()))
    matrix = [[str(c) for c in input().split()]for r in range(rows)]
    return matrix


matrix = read_matrix()
matrix_found = 0

for i in range(len(matrix)-1):
    for j in range(len(matrix[i])-1):
        if matrix[i][j]==matrix[i][j+1] and matrix[i][j]==matrix[i+1][j] and matrix[i][j]==matrix[i+1][j+1]:
            matrix_found+=1
print(matrix_found)