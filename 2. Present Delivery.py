def santa_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j


def movement(dx, dy, x, y):
    global n
    new_x = dx + x
    new_y = dy + y
    if 0 <= new_x < n and 0 <= new_y < n:
        return (new_x, new_y)
    else:
        new_x = x
        new_y = y
        return new_x, new_y


def happy_santa(new_x, new_y, presents, happy_kinds):
    if 0 <= new_x-1:
        if neighborhood[new_x-1][new_y] == "X" or neighborhood[new_x-1][new_y] =="V":
            presents-=1
            happy_kinds+=1
            neighborhood[new_x-1][new_y] = '-'
    if new_x+1 < n:
        if neighborhood[new_x+1][new_y] == "X" or neighborhood[new_x+1][new_y] =="V":
            presents-=1
            happy_kinds+=1
            neighborhood[new_x + 1][new_y] = '-'
    if 0 <= new_y-1:
        if neighborhood[new_x][new_y-1] == "X" or neighborhood[new_x][new_y-1] =="V":
            presents-=1
            happy_kinds+=1
            neighborhood[new_x][new_y - 1] = '-'
    if new_y+1 < n:
        if neighborhood[new_x][new_y+1] == "X" or neighborhood[new_x][new_y+1] =="V":
            presents-=1
            happy_kinds+=1
            neighborhood[new_x][new_y + 1] = '-'
    return presents, happy_kinds


presents = int(input())
n = int(input())
happy_kinds = 0
neighborhood = [[j for j in input().split()]for i in range(n)]
commands = input()
opr = {'up':(-1, 0), 'down':(1,0), 'left': (0, -1), 'right':(0,1)}
santa_current_position = santa_position(neighborhood)
while not commands == "Christmas morning" and presents>0:
    x, y = santa_current_position
    dx, dy = opr[commands]
    new_x, new_y = movement(dx,dy,x, y)
    if neighborhood[new_x][new_y] == 'X':
        neighborhood[new_x][new_y] = 'S'
        neighborhood[x][y] = '-'
        santa_current_position = new_x, new_y
    elif neighborhood[new_x][new_y] == 'V':
        neighborhood[new_x][new_y] = 'S'
        neighborhood[x][y] = '-'
        santa_current_position = new_x, new_y
        happy_kinds+=1
        presents-=1
    elif neighborhood[new_x][new_y]=='C':
        neighborhood[new_x][new_y]='S'
        neighborhood[x][y]='-'
        santa_current_position = new_x, new_y
        presents, happy_kinds = happy_santa(new_x, new_y, presents, happy_kinds)
    else:
        neighborhood[new_x][new_y] = 'S'
        neighborhood[x][y] = '-'
        santa_current_position = new_x, new_y

    commands = input()

if presents<=0:
    for row in neighborhood:
        if "V" in row:
            print("Santa ran out of presents!")
            break
for row in neighborhood:
    print(' '.join(row))
count_v=0
for row in neighborhood:
    if "V" in row:
        count_v+=1
if count_v == 0:
    print(f'Good job, Santa! {happy_kinds} happy nice kid/s.')
else:
    print(f'No presents for {count_v} nice kid/s.')