length_n, length_m = tuple(map(int, input().split()))

set_n = set()
set_m = set()

for i in range(length_m+length_n):
    inputs = input()
    if i >= length_m:
        set_n.add(inputs)
    else:
        set_m.add(inputs)
mutual_elements = set_m & set_n
print("\n".join(mutual_elements))