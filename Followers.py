commands = input()
users={}
while not commands == "Log out":
    args = commands.split(": ")
    command = args[0]
    username= args[1]
    if command == "New follower":
        if username in users:
            commands = input()
            continue
        users[username]= {}
        users[username]['l'] = 0
        users[username]['c'] = 0
    elif command == "Like":
        count = int(args[2])
        if username not in users:
            users[username] = {}
            users[username]['l'] = count
            users[username]['c'] = 0
        else:
            users[username]['l']+=count
    elif command == "Comment":
        if username not in users:
            users[username] ={}
            users[username]['c'] = 1
            users[username]['l'] = 0
        else:
            users[username]['c'] += 1
    elif command == "Blocked":
        if username not in users:
            print(f"{username} doesn't exist.")
        else:
            del users[username]
    commands = input()

print(f"{len(users)} followers")
sorted_users = sorted(users.keys(), key = lambda u:(-users[u]['l'], u))
for user in sorted_users:
    print(f"{user}: {users[user]['c']+users[user]['l']}")