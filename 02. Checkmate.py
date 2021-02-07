def king_position(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "K":
                return i, j


def queen_movement(r, j):
    global checkbox
    temp_r = r
    temp_j = j
    for right in range(j+1, n):
        if checkbox[temp_r][right] == "Q":
            break
        elif checkbox[temp_r][right] == "K":
            return True
    temp_r = r
    temp_j = j
    for left in range(j-1, -1, -1):
        if checkbox[temp_r][left] == "Q":
            break
        elif checkbox[temp_r][left] == "K":
            return True
    temp_r = r
    temp_j = j
    for down in range (r+1, n):
        if checkbox[down][temp_j] == "Q":
            break
        elif checkbox[down][temp_j] == "K":
            return True
    temp_r = r
    temp_j = j
    for up in range (r-1, -1, -1):
        if checkbox[up][temp_j] == "Q":
            break
        elif checkbox[up][temp_j] == "K":
            return True
    temp_r = r
    temp_j = j
    for up_right in range (r-1, -1, -1):
        if temp_j+1<n:
            temp_j+=1
            if checkbox[up_right][temp_j] == "Q":
                break
            elif checkbox[up_right][temp_j] == "K":
                return True
        else:
            break
    temp_r = r
    temp_j = j
    for up_left in range (r-1,-1, -1):
        if temp_j-1>=0:
            temp_j -= 1
            if checkbox[up_left][temp_j] == "Q":
                break
            elif checkbox[up_left][temp_j] == "K":
                return True
        else:
            break
    temp_r = r
    temp_j = j
    for down_right in range (r+1, n):
        if temp_j+1<n:
            temp_j += 1
            if checkbox[down_right][temp_j] == "Q":
                break
            elif checkbox[down_right][temp_j] == "K":
                return True
        else:
            break
    temp_r = r
    temp_j = j
    for down_left in range (r+1,n):
        if temp_j-1>=0:
            temp_j -= 1
            if checkbox[down_left][temp_j] == "Q":
                break
            elif checkbox[down_left][temp_j] == "K":
                return True
        else:
            break
    return False


final=True
n = 8
checkbox = [[j for j in input().split()]for i in range(n)]
# print(checkbox)
for r in range(len(checkbox)):
    for j in range(len(checkbox[r])):
        is_king_taken = False
        if checkbox[r][j] == "Q":
            is_king_taken = queen_movement(r, j)
        if is_king_taken:
            final = False
            print(f'[{r}, {j}]')
if final:
    print('The king is safe!')