def boomb(row, col, matrix):
    boomb_value = matrix[row][col]
    if matrix[row][col] > 0:
        matrix[row][col] = 0
        if col + 1 < len(matrix[row]) and matrix[row][col+1]>0:
            matrix[row][col+1]-=boomb_value
        if col - 1 >= 0 and matrix[row][col - 1]>0:
            matrix[row][col - 1] -= boomb_value
        if row +1 <len(matrix) and matrix[row + 1][col]>0:
            matrix[row + 1][col] -= boomb_value
        if row - 1 >= 0 and matrix[row - 1][col]>0:
            matrix[row - 1][col] -= boomb_value
        if row -1 >=0 and col -1 >=0 and matrix[row - 1][col-1]>0:
            matrix[row - 1][col-1] -= boomb_value
        if row + 1<len(matrix) and col - 1>=0 and matrix[row + 1][col - 1]>0:
            matrix[row + 1][col - 1] -= boomb_value
        if row + 1<len(matrix) and col + 1<len(matrix[row]) and matrix[row + 1][col + 1]>0:
            matrix[row + 1][col + 1] -= boomb_value
        if row - 1>=0 and col + 1<len(matrix[row]) and matrix[row - 1][col + 1]>0:
            matrix[row - 1][col + 1] -= boomb_value
    return matrix


n = int(input())
matrix = [[int(j) for j in input().split()]for i in range(n)]
coordinate = list(map(str, input().split()))
alive_cells = 0
cells_sum = 0
for c in coordinate:
    i, j = [int (x) for x in c.split(",")]
    boomb(i, j, matrix)

for row in range (len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col]>0:
            alive_cells+=1
            cells_sum+=matrix[row][col]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")

for row in range (len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end= " ")
    print()