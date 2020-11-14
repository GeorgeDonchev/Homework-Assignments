from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = deque([int(x) for x in input().split()][::-1])
locks = deque([int(l) for l in input().split()])
intelligence = int(input())

currant_barrel = barrel_size
bullets_count =0
barrels_count = 0
while bullets and locks:
    currant_barrel -= 1
    bullets_count+=1
    current_bullet = bullets.popleft()
    currant_lock = locks.popleft()
    if current_bullet <= currant_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(currant_lock)
    if currant_barrel == 0 and bullets:
        # barrels_count+=1
        currant_barrel = barrel_size
        print("Reloading!")


if not locks:
    money_earned = intelligence - (bullets_count*bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")