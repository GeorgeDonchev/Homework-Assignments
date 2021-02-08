def get_magic_triangle(n):
    matrix = [[1], [1,1]]
    for row in range(2, n):
        new_row = []
        for col in range(0, row+1):
            if col -1 < 0:
                new_row.append(1)
            elif col >= len(matrix[row-1]):
                new_row.append(1)
            else:
                upper_left = matrix[row-1][col-1]
                upper = matrix[row-1][col]
                new_value = upper_left + upper
                new_row.append(new_value)
        matrix.append(new_row)
    return matrix


print(get_magic_triangle(5))
new_matrix = get_magic_triangle(5)
for r in new_matrix:
    print(" ".join(map(str, r)))