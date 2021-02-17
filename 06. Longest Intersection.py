def filling_set(a,b, set_y):
    for e in range(a, b):
        set_n.add()

n = int(input())
longest_intersection = set()
for _ in range(n):
    current_intersection = set()
    set_n = set()
    set_m = set()
    n, m = tuple(map(str, input().split("-")))
    start_n, end_n = tuple(map(int, n.split(",")))
    start_m, end_m = tuple (map (int, m.split (",")))
    for e in range(start_n, end_n+1):
        set_n.add(e)
    for j in range(start_m, end_m+1):
        set_m.add(j)

    current_intersection = set_n & set_m
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")