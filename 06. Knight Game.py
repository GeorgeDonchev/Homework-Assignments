def get_damage(row, col, matrix):
    counter =0
    if row - 2 >= 0 and col - 1 >=0:
        if matrix[row-2][col-1] == "K":
            counter+=1
    if row -2 >=0 and col +1 <len(matrix):
        if matrix[row-2][col+1]=="K":
            counter+=1
    if row - 1>=0 and col-2>=0:
        if matrix[row-1][col-2]=="K":
            counter+=1
    if row -1>=0 and col +2 <len(matrix):
        if matrix[row-1][col+2]=="K":
            counter+=1
    if row+1<len(matrix) and col-2>=0:
        if matrix[row+1][col-2]=="K":
            counter+=1
    if row+1<len(matrix) and col+2<len(matrix):
        if matrix[row+1][col+2] == "K":
            counter+=1
    if row +2 <len(matrix) and col-1>=0:
        if matrix[row+2][col-1]=="K":
            counter+=1
    if row + 2<len(matrix) and col+1<len(matrix):
        if matrix[row+2][col+1]=="K":
            counter+=1
    return counter


n = int(input())
matrix = [[str(j) for j in input()]for i in range(n)]

replaced_knight = 0
max_damage = 0
danger_position = []
while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "K":
                current_counter = get_damage(i,j, matrix)
                if max_damage < current_counter:
                    max_damage = current_counter
                    danger_position = [i,j]

    if max_damage == 0:
        break
    danger_r, danger_c = danger_position
    matrix[danger_r][danger_c] = "0"
    max_damage = 0
    danger_position = []
    replaced_knight += 1

print(replaced_knight)