string = input()
commands = input()

while commands != "Sign up":
    tokens = commands.split()
    command = tokens[0]

    if command == "Case":
        state = tokens[1]
        if state == "lower":
            string = string.lower()
        else:
            string = string.upper()
        print(string)
    elif command == "Reverse":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        substring = ""
        if len(string) <= end_index or end_index < 0 or len(string)<=start_index or start_index < 0:
            commands = input()
            continue
        substring = string[start_index:end_index+1]
        substring =substring[::-1]
        print(substring)
    elif command == "Cut":
        sub_s = tokens[1]
        if sub_s not in string:
            print(f"The word {string} doesn't contain {sub_s}.")
        else:
            string = string.replace(sub_s, "")
            print(string)
    elif command == "Replace":
        char = tokens[1]
        string = string.replace(char, '*')
        print(string)
    elif command == "Check":
        char = tokens[1]
        if char in string:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    commands = input()