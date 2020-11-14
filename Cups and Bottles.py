from collections import deque
cups = deque([int(c) for c in input().split()])
bottles = deque([int(b) for b in input().split()][::-1])
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.popleft()
    if current_cup - current_bottle < 0:
        wasted_water += (current_cup - current_bottle)
    elif current_cup - current_bottle > 0:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
if not cups:
    bottles = [str(i) for i in bottles]
    print(f"Bottles: {' '.join(bottles)}")
elif not bottles:
    cups = [str(i) for i in cups]
    print (f"Cups: {' '.join (cups)}")
print(f"Wasted litters of water: {abs(wasted_water)}")

