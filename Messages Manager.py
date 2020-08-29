capacity = int(input())
commands = input()
users={}
while not commands == "Statistics":
    tokens = commands.split('=')
    command = tokens[0]
    if command == "Add":
        user_name = tokens[1]
        sent_message = int(tokens[2])
        received_message = int(tokens[3])
        if user_name not in users:
            users[user_name]={}
            users[user_name]['sent'] = sent_message
            users[user_name]['received'] = received_message
    elif command == "Message":
        sender = tokens[1]
        receiver = tokens[2]
        if sender in users and receiver in users:
            users[sender]['sent'] += 1
            users[receiver]['received'] += 1
            if users[sender]['sent'] + users[sender]['received'] == capacity:
                del users[sender]
                print(f"{sender} reached the capacity!")
            if users[receiver]['received'] + users[receiver]['sent'] == capacity:
                del users[receiver]
                print (f"{receiver} reached the capacity!")
    elif command == "Empty":
        username = tokens[1]
        if username == "All":
            users.clear()
        elif username in users:
            del users[username]
    commands = input()
print(f"Users count: {len(users)}")
sorted_users = sorted(users.keys(), key=lambda u: (-users[u]['received'], u[0]))
for user in sorted_users:
    print(f"{user} - {users[user]['sent']+users[user]['received']}")