n = int(input())
matrix = [[j for j in map(int, input().split(", "))]for i in range(n)]
primary_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if i == j]
the_sum = sum(primary_diagonal)
primary_diagonal = [str(s) for s in primary_diagonal]
print("First diagonal:",', '.join(primary_diagonal), end = "")
print(f'. Sum: {the_sum}')
secondary_diagonal = [matrix[i][j] for i in range(n) for j in range(n) if j == n - 1 - i]
the_sum_s = sum(secondary_diagonal)
secondary_diagonal = [str(s) for s in secondary_diagonal]
print("Second diagonal:",', '.join(secondary_diagonal), end = "")
print(f'. Sum: {the_sum_s}')
