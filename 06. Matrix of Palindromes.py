rows, cols = tuple(map(int, input().split()))
matrix = [[chr(97+i)+chr(97+j+i)+chr(97+i) for j in range(cols)]for i in range(rows)]
[[print(matrix[i][j], end = " ")if j < len(matrix[i])-1  else print(matrix[i][j]) for j in range(len(matrix[i]))]for i in range(len(matrix))]