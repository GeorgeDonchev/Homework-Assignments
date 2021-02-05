command = input()
res = 0
numbers = [i for i in map(int, input().split())]
if command == "Odd":
    res = sum(filter(lambda x: x % 2 == 1, numbers)) * len(numbers)
elif command == "Even":
    res = sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)
print(res)