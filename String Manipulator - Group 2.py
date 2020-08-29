text = input()

commands = input()
index = 0
while not commands == "Done":
    args = commands.split()
    command = args[0]

    if command == "Change":
        char = args[1]
        char_replace = args[2]
        text = text.replace(char, char_replace)
        print(text)
    elif command == "Includes":
        substring = args[1]
        if substring in text:
            print("True")
        else:
            print("False")
    elif command == "End":
        subs = args[1]
        print(text.endswith(subs))
    elif command == "Uppercase":
        text = text.upper()
        print(text)
    elif command == "FindIndex":
        char = args[1]
        index = text.index(char)
        print(index)
    elif command == "Cut":
        start_index = int(args[1])
        length = int(args[2])
        end_index=start_index+length
        text = text[start_index:end_index]
        print(text)
    commands = input()