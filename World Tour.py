destinations = input ()
commands = input()
while not commands == "Travel":
    args = commands.split (':')
    command = args[0]

    if command == "Add Stop":
        index = int(args[1])
        string = args[2]
        if 0<=index<=len(destinations):
            destinations = destinations[:index]+string+destinations[index:]
    elif command == "Remove Stop":
        start_index = int(args[1])
        end_index = int(args[2])+1
        if 0 <= start_index <=len(destinations) and 0 < end_index <=len(destinations):
            destinations = destinations[:start_index] + destinations[end_index:]
            # print(destinations)
    elif command == "Switch":
        old_string = args[1]
        new_string = args[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
    print(destinations)
    commands = input()
print(f"Ready for world tour! Planned stops: {destinations}")