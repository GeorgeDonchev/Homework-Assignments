rows = int(input())
flat_matrix = [element for sublist in range(rows) for element in map(int,input().split(", "))]
print(flat_matrix)
