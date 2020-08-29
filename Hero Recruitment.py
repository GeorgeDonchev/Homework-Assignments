commands = input()
spellbook ={}
while not commands == "End":
    tokens = commands.split()
    command = tokens[0]
    hero_name = tokens[1]
    if command == "Enroll":
        if hero_name not in spellbook:
            spellbook[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command == "Learn":
        spell_name = tokens[2]
        if hero_name not in spellbook:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in spellbook[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            spellbook[hero_name].append(spell_name)

    elif command == "Unlearn":
        spell_name = tokens[2]
        if hero_name not in spellbook:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in spellbook[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            spellbook[hero_name].remove(spell_name)

    commands = input()
print("Heroes:")
for k,v in sorted(spellbook.items(), key = lambda s: (-len(s[1]), s[0])):
    print(f"== {k}: {', '.join(v)}")

