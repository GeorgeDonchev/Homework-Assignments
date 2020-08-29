lines = input()
usernames ={}
while not lines == "Statistics":
    tokes = lines.split('->')
    command = tokes[0]
    user_name = tokes[1]
    if command == "Add":
        if user_name not in usernames:
            usernames[user_name] = []
        else:
            print(f"{user_name} is already registered")
    elif command == "Send":
        e_mail=tokes[2]
        if user_name not in usernames:
            lines = input()
            continue
        usernames[user_name].append(e_mail)
    elif command == "Delete":
        if user_name in usernames:
            del usernames[user_name]
        else:
            print(f"{user_name} not found!")
    lines = input()
print(f"Users count: {len(usernames)}")

for key, value in sorted(usernames.items(), key = lambda u: (-len(u[1]), u[0])):
    print(key)
    if value:
        print(" - ", end = "")
    print ("\n - ".join (value))