people = int(input())
unique_people = set()
for _ in range(people):
    inputs = input()
    unique_people.add(inputs)

print('\n'.join(unique_people))
