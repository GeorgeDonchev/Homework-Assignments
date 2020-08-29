password = input()
commands = input()

while not commands == 'Done':
    tokens = commands.split()
    command = tokens[0]

    if command == "TakeOdd":
        new_password = ""
        for p in range(len(password)):
            if p % 2 == 1:
                new_password+=password[p]
        password = new_password
        print(password)
    elif command == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        end = index + length
        password = password[:index] + password[end:]
        print(password)
    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    commands = input()

print(f"Your password is: {password}")