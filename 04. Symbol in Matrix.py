def read_matrix():
    n = int(input())
    matrix = [list(map(str, input())) for x in range(n)]
    return matrix


matrix = read_matrix()
special_symbol = input()
is_found = False
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == special_symbol:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"({r}, {c})")
else:
    print(f"{special_symbol} does not occur in the matrix")

