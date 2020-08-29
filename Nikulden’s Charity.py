text = input()
commands = input()
current_string = ""
while not commands == "Finish":
    tokens = commands.split()
    command = tokens[0]
    if command == "Replace":
        current_char = tokens[1]
        new_char = tokens[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif command == "Cut":
        start_index = int(tokens[1])
        end_index = int(tokens[2])+1
        if len(text)<=end_index or end_index<=start_index or start_index<0:
            print("Invalid indexes!")
            commands = input()
            continue
        text = text[:start_index]+text[end_index:]
        print(text)
    elif command == "Make":
        if tokens[1] == "Upper":
            text=text.upper()
        elif tokens[1] == "Lower":
            text=text.lower()
        print(text)
    elif command == "Check":
        string = tokens[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command == "Sum":

        start_index = int(tokens[1])
        end_index = int(tokens[2])+1
        if len(text)<=end_index or end_index<=start_index or start_index<0:
            print("Invalid indexes!")
            commands = input()
            continue
        current_string = text[start_index:end_index]
        sub_sring_sum=0
        for ch in current_string:
            sub_sring_sum+=ord(ch)
        print(sub_sring_sum)
    commands = input()

