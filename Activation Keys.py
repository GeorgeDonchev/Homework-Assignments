raw_activation_key = input()
commands = input()

while not commands == "Generate":
    args=commands.split(">>>")
    command = args[0]

    if command == "Contains":
        substring = args[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        font = args[1]
        start_index = int(args[2])
        end_index = int(args[3])
        if font == "Upper":
            raw_activation_key = raw_activation_key[:start_index]+ raw_activation_key[start_index: end_index].upper()+raw_activation_key[end_index:]
        else:
            raw_activation_key = raw_activation_key[:start_index]+ raw_activation_key[start_index: end_index].lower()+raw_activation_key[end_index:]
        print(raw_activation_key)
    elif command == "Slice":
        start_index = int(args[1])
        end_index = int(args[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    commands = input()
print(f"Your activation key is: {raw_activation_key}")