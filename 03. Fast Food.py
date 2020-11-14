food_qty=int(input())
orders = list(map(int, input().split()))
completed_orders = []
orders_left = []
for order in orders:
    if food_qty - order >= 0:
        food_qty -= order
        completed_orders.append(order)
    else:
        orders_left.append(order)
print(max(completed_orders))

if len(completed_orders) == len(orders):
    print("Orders complete")
else:
    print("Orders left:", end= " ")
    for i in range(len(orders_left)):
        print(f"{orders_left[i]}", end = " ")
