from collections import deque
people = deque(input().split(" "))
n_toss = int (input())

while len(people) > 1:
    people.rotate(-n_toss)
    print(f"Removed {people.pop()}")
print(f"Last is {people[0]}")