number_of_cars = int(input())

parking = set()

for _ in range(number_of_cars):
    command, car_id = input().split(", ")
    if command == "IN":
        parking.add(car_id)
    elif command == "OUT" and car_id in parking:
        parking.remove(car_id)
# parking =list(parking)
if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")
