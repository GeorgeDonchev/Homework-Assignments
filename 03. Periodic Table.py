n = int(input())
unique_elements = set()
for _ in range(n):
    inputs = input().split()
    for e in inputs:
        unique_elements.add(e)
print("\n".join(unique_elements))

