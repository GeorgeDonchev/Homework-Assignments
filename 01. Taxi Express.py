from collections import deque

customers_numbers = deque(map(int, input().split(", ")))
taxis_numbers = list(map(int, input().split(", ")))
total_time = 0

while customers_numbers and taxis_numbers:
    current_customer_time = customers_numbers.popleft()
    current_taxi_time = taxis_numbers.pop()
    if current_taxi_time >= current_customer_time:
        total_time+=current_customer_time
    else:
        customers_numbers.appendleft(current_customer_time)
if not customers_numbers:
    print("All customers were driven to their destinations")
    print(f'Total time: {total_time} minutes')
else:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(map(str, customers_numbers))}')
