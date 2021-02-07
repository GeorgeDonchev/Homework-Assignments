def find_beggining(materix):
    for r in range(len(materix)):
        for c in range(len(materix[r])):
            if materix[r][c]=="p":
                return r, c


def move(tup_1, dx, dy):
    new_x = tup_1[0] + dx
    new_y = tup_1[1] + dy
    return new_x, new_y


def move_with_step(position, step):
    global pos
    if position == "right" or position == "left":
        dy = pos[position][1] * int(step)
        dx = pos[position][0]
    elif position == "up" or position == "down":
        dx = pos[position][0] * int(step)
        dy = pos[position][1]
    return dx, dy


n = int(input())
territory = [[c for c in input().split()]for r in range(n)]
m = int(input())
plane_pos = find_beggining(territory)
pos = {"right":(0,1), "left":(0,-1), "up":(-1, 0), "down":(1,0)}
destroyed_t = 0
count_t = 0
for rows in territory:
    if "t" in rows:
        count_t+=1
is_target_succeed = False
for _ in range(m):
    action, position, step = input().split()
    x, y = plane_pos
    dx, dy = move_with_step(position, step)
    new_x, new_y = move(plane_pos, dx, dy)
    if action == "move":
        if 0 <= new_x < n and 0 <= new_y < n and territory[new_x][new_y] == "." and not territory[new_x][new_y] == "x":
            territory[x][y] = "."
            territory[new_x][new_y] = "p"
            plane_pos = new_x,  new_y
    elif action == "shoot":
        if 0 <= new_x < n and 0 <= new_y < n:
            if territory[new_x][new_y] == "t":
                destroyed_t+=1
                count_t-=1
            territory[new_x][new_y] = "x"
    if count_t == 0:
        is_target_succeed = True
        break


if is_target_succeed:
    print(f"Mission accomplished! All {destroyed_t} targets destroyed.")
else:
    print(f"Mission failed! {count_t} targets left.")

for rows in territory:
    print(" ".join(rows))