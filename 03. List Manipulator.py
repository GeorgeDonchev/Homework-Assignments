from collections import deque


def list_manipulator(numbers, *args_com):
    new_numbers = deque(numbers)
    if args_com[0] == "add":
        if args_com[1] == "beginning":
            if len(args_com) >3:
                for number in range(len(args_com)-1, 1, -1):
                    new_numbers.appendleft(args_com[number])
            else:
                new_numbers.appendleft(args_com[2])
        elif args_com[1] == "end":
            if len (args_com) >3:
                for number in range (2, len(args_com)):
                    new_numbers.append(args_com[number])
            else:
                new_numbers.append(args_com[2])

    elif args_com[0] == "remove":
        if len(args_com)>2:
            for _ in range(args_com[2]):
                if args_com[1] == 'beginning':
                    new_numbers.popleft()
                elif args_com[1] == 'end':
                    new_numbers.pop()
        else:
            if args_com[1] == 'beginning':
                new_numbers.popleft()
            elif args_com[1] == 'end':
                new_numbers.pop()

    return list(new_numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
