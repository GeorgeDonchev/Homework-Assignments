import re

destination = input()
pattern = r"(=|/)([A-Z]{1}[a-z]{2,})\1"
matches = re.findall(pattern, destination)
travel_points = 0
valid_destinations = []
if not matches:
    print("Destinations:")
else:
    for match in matches:
        travel_points+=len(match[1])
        valid_destinations.append(match[1])
    print (f"Destinations: {', '.join (valid_destinations)}")

print(f"Travel Points: {travel_points}")
