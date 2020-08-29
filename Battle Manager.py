commands = input()
persons={}
while not commands == "Results":
    args = commands.split(':')
    command = args[0]

    if command == "Add":
        person_name = args[1]
        health = int(args[2])
        energy = int(args[3])
        if person_name not in persons:
            persons[person_name] = {}
            persons[person_name]['h'] = 0
            persons[person_name]['e'] = 0
            persons[person_name]['e'] += energy

        persons[person_name]['h'] += health

    elif command == "Attack":
        attacker_name = args[1]
        defender_name = args[2]
        damage = int(args[3])
        if attacker_name in persons and defender_name in persons:
            persons[defender_name]['h'] -= damage
            persons[attacker_name]['e'] -= 1
            if persons[defender_name]['h'] <= 0:
                del persons[defender_name]
                print(f"{defender_name} was disqualified!")
            if persons[attacker_name]['e'] == 0:
                del persons[attacker_name]
                print(f"{attacker_name} was disqualified!")

    elif command == "Delete":
        username = args[1]
        if username == "All":
            persons.clear()
            commands = input()
            continue
        if username in persons:
            del persons[username]

    commands = input()

print(f"People count: {len(persons)}")
sorted_persons = sorted(persons.keys(), key = lambda p: (-persons[p]['h'], p))
for person in sorted_persons:
    print(f"{person} - {persons[person]['h']} - {persons[person]['e']}")