from collections import deque
queue = deque([])
while True:
    command = input()
    if command == "Paid":
        while len(queue) > 0:
            print(queue.popleft())
    elif command == "End":
        break
    else:
        name = command
        queue.append(name)
print(f"{len(queue)} people remaining.")
