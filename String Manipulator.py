string = input()
commands = input()

while commands != 'End':
    tokens = commands.split()
    command = tokens[0]
    if command == "Translate":
        char = tokens[1]
        new_char = tokens[2]
        string = string.replace(char, new_char)
        print(string)
    elif command == "Includes":
        substring = tokens[1]
        if substring in string:
            print('True')
        else:
            print("False")
    elif command == "Start":
        sub_string = tokens[1]
        index = len(sub_string)
        if sub_string == string[:index]:
            print('True')
        else:
            print("False")
    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = tokens[1]
        for i in range(len(string)-1,-1, -1):
            if char == string[i]:
                print(i)
                break

    elif command == "Remove":
        start_index = int(tokens[1])
        count = int(tokens[2])
        string_to_remove=string[start_index:start_index+count]
        string = string.replace(string_to_remove, "")
        print(string)
    commands = input()
