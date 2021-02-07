from collections import deque


bomb_effect = deque(map(int, input().split(", ")))
bomb_casing = list(map(int, input().split(", ")))

bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
bombs_ref = {"Datura Bombs": 40, "Cherry Bombs": 60, "Smoke Decoy Bombs": 120}
bomb_casing_filled = False

while bomb_casing and bomb_casing and not bomb_casing_filled:
    is_bomb = False
    current_bomb_effect = bomb_effect.popleft()
    current_bomb_casing = bomb_casing.pop()
    current_bomb = current_bomb_effect + current_bomb_casing
    for values in bombs_ref.keys():
        if bombs_ref[values] == current_bomb:
            bombs[values] += 1
            is_bomb = True
            break
    if all(values>=3 for values in bombs.values()):
        bomb_casing_filled = True
        break

    if not is_bomb:
        current_bomb_casing -= 5
        if current_bomb_casing >= 0:
            bomb_effect.appendleft(current_bomb_effect)
            bomb_casing.append(current_bomb_casing)

if bomb_casing_filled:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")
print(f'Bomb Effects: {", ".join(map(str, bomb_effect)) if bomb_effect else "empty"}')
print(f'Bomb Casings: {", ".join(map(str, bomb_casing)) if bomb_casing else "empty"}')

for k, v in sorted(bombs.items()):
    print(f"{k}: {v}")



