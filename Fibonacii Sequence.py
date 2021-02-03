import fibonacci
commands = input()

while not commands == "Stop":
    args = commands.split()
    command = args[0]

    if command == "Create":
        value = int(args[-1])
        fib=fibonacci.sequence(value)
        print(" ".join([str(x) for x in fib]))
    elif command == "Locate":
        number = int(args[1])
        if number in fib:
            print(f"The number - {number} is at index {fib.index(number)}")
        else:
            print(f"The number {number} is not in the sequence")
    commands = input()
