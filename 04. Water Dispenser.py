from collections import deque
water_in_dispenser = int(input())
people_to_drink = deque([])

while True:
    command = input()
    if command == "Start":
        break
    else:
        people_to_drink.append(command)

while True:
    commands = input()
    if commands.isdigit():
        litters_to_drink = int(commands)
        person = people_to_drink.popleft()
        if water_in_dispenser - litters_to_drink >= 0:
            water_in_dispenser-=litters_to_drink
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

    elif commands.startswith("refill"):
        args = commands.split (" ")
        refill = int(args[1])
        water_in_dispenser+=refill
    elif commands == "End":
        break
print(f"{water_in_dispenser} liters left")