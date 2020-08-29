n = int(input())
plants={}
for _ in range(n):
    args = input().split('<->')
    plant = args[0]
    rarity = int(args[1])
    if plant not in plants:
        plants[plant]= {}
        plants[plant]['rarity'] = rarity
        plants[plant]['rating'] = 0
        plants[plant]['c'] = 0
    else:
        plants[plant]['rarity']+=rarity

commands = input()

while not commands == "Exhibition":
    if ':' in commands:
        commands = commands.replace(': ', ' - ')
    tokens = commands.split()
    command = tokens[0]
    plant = tokens[2]
    if command == "Rate":
        rating = int(tokens[4])
        if plant in plants:
            plants[plant]['rating']+=rating
            plants[plant]['c'] += 1
        else:
            print('error')
    elif command == "Update":
        new_rarity = int(tokens[4])
        if plant in plants:
            plants[plant]['rarity']=new_rarity
        else:
            print('error')
    elif command == "Reset":
        if plant in plants:
            plants[plant]['rating'] = 0
            plants[plant]['c'] = 0
        else:
            print("error")
    commands = input()
print("Plants for the exhibition:")
for k in plants.keys():
    if not plants[k]['rating'] == 0:
        plants[k]['rating']=plants[k]['rating']/plants[k]['c']
    # else:
    #     plants[k]['rating'] = 0
    del plants[k]['c']

sorted_plants = sorted(plants.keys(), key = lambda p: (-plants[p]['rarity'], -plants[p]['rating']))
for pl in sorted_plants:
    print(f"- {pl}; Rarity: {plants[pl]['rarity']}; Rating: {plants[pl]['rating']:.2f}")