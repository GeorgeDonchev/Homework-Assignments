commands = input()
roads={}
while not commands == "END":
    args = commands.split('->')
    command = args[0]
    road = args[1]
    if command == "Add":
        race_name = args[2]
        if road not in roads:
            roads[road]=[]

        roads[road].append(race_name)
    elif command == 'Move':
        racer_name = args[2]
        next_road = args[3]
        for r in roads.values():
            if racer_name in r:
                roads[road].remove(racer_name)
                roads[next_road].append(racer_name)
                break

    elif command == 'Close':
        if road in roads:
            del roads[road]
    commands = input()
print("Practice sessions:")
for k, v in sorted(roads.items(), key=lambda r: (-len(r[1]), r[0])):
    print(k)
    print('++', end='')
    print('\n++'.join(v))