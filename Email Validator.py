e_mail = input()
commands = input()

while not commands == "Complete":
    arg = commands.split()
    command = arg[0]

    if command == "Make":
        cmd = arg[1]
        if cmd == "Upper":
            e_mail = e_mail.upper()
        elif cmd == "Lower":
            e_mail = e_mail.lower()
        print(e_mail)
    elif command == "GetDomain":
        current_domain=""
        index = int(arg[1])
        current_domain = e_mail[-index::]
        print(current_domain)
    elif command == "GetUsername":
        if "@" not in e_mail:
            print(f"The email {e_mail} doesn't contain the @ symbol.")
        else:
            substring = e_mail.split("@")
            user_name = substring[0]
            print(user_name)
    elif command == "Replace":
        char = arg[1]
        e_mail=e_mail.replace(char, "-")
        print(e_mail)
    elif command == "Encrypt":
        for symbol in e_mail:
            print(ord(symbol), end = " ")
    commands = input()