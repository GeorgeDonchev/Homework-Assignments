from collections import deque
green_light_duration = int(input())
free_window = int(input())
command = input()
cars = deque()
is_accident = False
cars_passed = []
while not command == "END":
    cars.append(command)
    command = input()
traffic_timer = green_light_duration
while cars:
    current_car = cars.popleft()
    if current_car == "green":
        traffic_timer = green_light_duration
        continue
    if traffic_timer > 0:
        if traffic_timer >= len(current_car):
            traffic_timer -= len(current_car)
            cars_passed.append(current_car)
        elif traffic_timer + free_window >= len(current_car):
            traffic_timer = 0
            cars_passed.append(current_car)
        else:
            index = traffic_timer+free_window
            hit = current_car[index]
            print("A crash happened!")
            print(f"{current_car} was hit at {hit}.")
            is_accident = True
            break

if not is_accident:
    print("Everyone is safe.")
    print(f"{len(cars_passed)} total cars passed the crossroads.")

