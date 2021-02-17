def int_to_str(integer):
    new_value = [str(x) for x in integer]
    return new_value

n = int(input())
set_odd_number = set()
set_even_number = set()
for i in range(1, n+1):
    name = input()
    summed_value_name = 0
    for char in name:
        summed_value_name += ord(char)
    summed_value_name //= i
    if summed_value_name % 2 == 0:
        set_even_number.add(summed_value_name)
    else:
        set_odd_number.add(summed_value_name)
total_odd = sum(set_odd_number)
total_even = sum(set_even_number)
if total_odd == total_even:
    union = set_odd_number | set_even_number
    union = [str(x) for x in union]
    print(", ".join(union))
elif total_even < total_odd:
    difference = set_odd_number - set_even_number
    difference = [str(x) for x in difference]
    print (", ".join (difference))
else:
    sim_difference = set_odd_number ^ set_even_number
    sim_difference = [str(x) for x in sim_difference]
    print(", ".join(sim_difference))