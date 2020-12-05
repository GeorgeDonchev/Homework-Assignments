heroes = input().split(", ")
heroes_itms = {}
heroes_costs = {}
commands = input()
while not commands == "End":
    name, item, cost = tuple(commands.split("-"))
    if name not in heroes_itms:
        heroes_itms[name] = []
        heroes_costs [name] = []
    if item not in heroes_itms[name]:
        heroes_itms[name].append(item)
        heroes_costs[name].append(int(cost))
    commands = input()

combined = [print(f'{k} -> Items: {len(heroes_itms[k])}, Cost: {sum(heroes_costs[k])}') for k,v in zip(heroes_itms, heroes_costs)]


