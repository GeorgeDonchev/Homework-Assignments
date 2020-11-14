clothes_value = list(map(int, input().split()))
rack_capacity = int(input())
used_racks = 1
current_rack = rack_capacity
while clothes_value:
    value = clothes_value.pop()
    current_rack -= value
    if current_rack == 0:
        used_racks +=1
        current_rack = rack_capacity
    elif current_rack < 0:
        used_racks +=1
        current_rack = rack_capacity
        current_rack -= value

print(used_racks)

