command = input ()
cities = {}
while not command == "Sail":
    args = command.split ("||")
    city = args[0]
    population = int (args[1])
    gold = int (args[2])
    if not city in cities:
        cities[city] = {}
        cities[city]['population'] = population
        cities[city]['gold'] = gold
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    command = input ()

print(cities)
events = input ()

while not events == "End":
    tokens = events.split ("=>")
    event = tokens[0]

    if event == "Plunder":
        city = tokens[1]
        people = int (tokens[2])
        gold = int (tokens[3])
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print (f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            print (f"{city} has been wiped off the map!")

    elif event == "Prosper":
        current_gold = 0
        city = tokens[1]
        gold = int (tokens[2])
        if gold < 0:
            print ("Gold added cannot be a negative number!")
            events = input()
            continue
        cities[city]['gold'] += gold
        current_gold = cities[city]['gold']
        print (f"{gold} gold added to the city treasury. {city} now has {current_gold} gold.")
    events = input()

sorted_cities = sorted(cities.keys(), key = lambda c: (-cities[c]['gold'], c))
print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
for city in sorted_cities:
    print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
