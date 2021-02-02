def read_matrix():
    rows, cols = tuple(map(int, input().split()))
    matrix = [[str(j) for j in input().split() ] for i in range(rows)]
    return matrix


matrix = read_matrix()
commands = input()

while not commands == "END":
    args= commands.split()
    command = args[0]
    temp = None
    if command == "swap":
        (i1, j1, i2, j2) = tuple(map(int, args[1::]))
        if 0 <= i1<len(matrix) and 0 <= i2<len(matrix) and 0 <= j1<len(matrix[i1]) and 0 <= i2<len(matrix[i2]):
            temp = matrix[i2][j2]
            matrix[i2][j2] = matrix[i1][j1]
            matrix[i1][j1] = temp
            for row in matrix:
                for col in row:
                    print(col, end = " ")
                print()
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
    commands = input()
