text = input()
commands = input()

while not commands == "For Azeroth":
    tokens = commands.split()
    command = tokens[0]

    if command =="GladiatorStance":
        text=text.upper()
        print(text)
    elif command == "DefensiveStance":
        text = text.lower ()
        print(text)
    elif command == "Dispel":
        index = int(tokens[1])
        letter = tokens[2]
        if index<len(text):
            text = text[:index]+letter+text[index+1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command == "Target":
        if tokens [1] == "Change":
            substring = tokens[2]
            sec_substring = tokens[3]
            text = text.replace(substring, sec_substring)
            print(text)
        else:
            substring = tokens[2]
            text = text.replace(substring, "")
            print(text)
    else:
        print("Command doesn't exist!")

    commands = input()
