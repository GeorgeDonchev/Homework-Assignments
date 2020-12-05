n = int(input())
matrix = [[j for j in map(int, input().split())] for i in range(n)]
commands = input()
while commands != "END":
    command, row, col, value = commands.split()
    r_count = int(row)
    c_count = int(col)
    v = int(value)
    if command == "Add":
        if 0 <= r_count < n and 0 <= c_count < n:
            matrix[r_count][c_count]+=v
        else:
            print("Invalid coordinates")
    elif command == "Subtract":
        if 0 <= r_count < n and 0 <= c_count < n:
            matrix[r_count][c_count]-=v
        else:
            print ("Invalid coordinates")

    commands = input()
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()
