from collections import deque

petrol_pumps=int(input())
index = 0
pumps = deque()
for _ in range(petrol_pumps):
    pumps.append([int(x) for x in input().split()])
is_completed = False
while index < len(pumps):
    tank = 0
    for pump in pumps:
        (distance, fuel) = pump
        tank += distance - fuel
        if tank < 0:
            index += 1
            pumps.rotate(-1)
            break
    else:
        is_completed = True
        break
if is_completed:
    print(index)






