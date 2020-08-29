n = int(input())
heroes = {}
for _ in range(n):
    hero_info = input().split()
    hero_name = hero_info[0]
    hp = int(hero_info[1])
    mp = int(hero_info[2])

    if hero_name not in heroes:
        heroes[hero_name]={}
        heroes[hero_name]['hit']= hp
        heroes[hero_name]['mana'] = mp

commands = input()

while not commands == "End":
    tokens = commands.split(' - ')
    command = tokens[0]
    hero_name = tokens[1]
    if command == "CastSpell":
        mp = int(tokens[2])
        spell_name = tokens[3]
        if heroes[hero_name]['mana']>=mp:
            heroes[hero_name]['mana'] -= mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes[hero_name]['hit']-=damage
        if heroes[hero_name]['hit'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command == "Recharge":
        amount = int(tokens[2])
        if heroes[hero_name]['mana']+amount < 200:
            heroes[hero_name]['mana'] += amount
        else:
            amount = 200 - heroes[hero_name]['mana']
            heroes[hero_name]['mana'] = 200
        print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(tokens[2])
        if heroes[hero_name]['hit']+amount<100:
            heroes[hero_name]['hit'] += amount
        else:
            amount = 100-heroes[hero_name]['hit']
            heroes[hero_name]['hit'] = 100
        print(f"{hero_name} healed for {amount} HP!")

    commands = input()
sorted_heroes = sorted(heroes.keys(), key = lambda h: (-heroes[h]['hit'], h))

for key in sorted_heroes:
    print(key)
    print(f" HP: {heroes[key]['hit']}")
    print(f" MP: {heroes[key]['mana']}")