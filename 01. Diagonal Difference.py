def read_matrix():
    n = int(input())
    matrix = [[int(i) for i in input().split()] for x in range(n)]
    return matrix

matrix = read_matrix()

sum_primery =0
sum_secondary = 0

for i in range(len(matrix)):
    sum_primery += matrix[i][i]
    sum_secondary += matrix[i][len(matrix)-1-i]

print(abs(sum_primery-sum_secondary))