rows, columns = [int(x) for x in input().split(", ")]
matrix = [0 for r in range(rows)]

for r in range(rows):
    lines = [int(l) for l in input().split(", ")]
    matrix[r] = lines

sum_elements= 0

for row in range(rows):
    sum_elements+=sum(matrix[row])
print(sum_elements)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = " ")
    print()