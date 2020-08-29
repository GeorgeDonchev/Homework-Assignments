commands = input()
event={}
unliked_meals=[]
while not commands == "Stop":
    tokens = commands.split('-')
    command = tokens[0]
    guest = tokens[1]
    meal = tokens[2]
    if command == "Like":
        if guest not in event:
            event[guest]=[]
        if meal not in event[guest]:
            event[guest].append(meal)
    elif command == "Unlike":
        if guest not in event:
            print(f"{guest} is not at the party.")
        elif meal not in event[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            current_unliked_meal=""
            index=0
            index=event[guest].index(meal)
            current_unliked_meal=event[guest].pop(index)
            unliked_meals.append(current_unliked_meal)
            print(f"{guest} doesn't like the {meal}.")

    commands = input()

for key, value in sorted(event.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {len(unliked_meals)}")