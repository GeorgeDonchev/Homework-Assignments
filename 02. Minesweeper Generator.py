def calculation_cell_value(r, c, mines_field):
    current_cell_value = 0
    new_x = 0
    new_y = 0
    for pos in directions.values ():
        dx, dy = pos
        if r == 0 and c == 0 and dx >= 0 and dy >= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value+=1
        elif r == 0 and 0 < c < len (mines_field[r]) - 1 and dx >= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value+=1
        elif r == 0 and c == len (mines_field[r])-1 and dx > 0 and dy <= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif 0 < r < len (mines_field) - 1 and 0 < c < len (mines_field[r]) - 1:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif r == len(mines_field)-1 and c == 0 and dx <= 0 and dy >= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif r == len(mines_field)-1 and c == len(mines_field[r])-1 and dx <=0 and dy <= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif c == 0 and 0 < r < len (mines_field) - 1 and dy >=0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif c == len(mines_field[r])-1 and 0 < r < len (mines_field) - 1 and dy <= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
        elif r == len(mines_field)-1 and 0 < c < len (mines_field[r]) - 1 and dx <= 0:
            new_x, new_y = sum_dx_dy (r, c, dx, dy)
            if mines_field[new_x][new_y] == "*":
                current_cell_value += 1
    return current_cell_value


def sum_dx_dy(r, c, dx, dy):
    new_x = r + dx
    new_y = c + dy
    return new_x, new_y


directions = {"up": (-1, 0), "down": (1, 0), "l": (0, -1), "r": (0, 1), "uld": (-1, -1), "urd": (-1, 1), "dld": (1, -1),
              "drd": (1, 1)}
n = int (input ())
mines_field = [[" " for j in range (n)] for i in range (n)]
bombs = int (input ())
for _ in range (bombs):
    x, y = input ().split (", ")
    mines_field[int (x[-1])][int (y[0])] = "*"

for r in range (len (mines_field)):
    for c in range (len (mines_field[r])):
        if mines_field[r][c] == '*':
            continue
        current_cell_value= calculation_cell_value(r,c, mines_field)
        mines_field[r][c] = current_cell_value

for r in range(len(mines_field)):
    for c in range(len(mines_field[r])):
        print(mines_field[r][c], end = " ")
    print()
