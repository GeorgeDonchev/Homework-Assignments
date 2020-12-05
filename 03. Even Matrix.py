rows = int(input())
matrix = [[element for element in map(int, input().split(", ")) if element % 2 == 0] for row in range(rows)]
print(matrix)

