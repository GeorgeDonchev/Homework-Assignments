def read_matrix():
    n = int(input())
    matrix = [list(map(int, input().split())) for r in range(n)]
    return matrix
sum_primary_diagonal = 0

matrix = read_matrix()
for index in range(len(matrix)):
    sum_primary_diagonal+=matrix[index][index]
print(sum_primary_diagonal)