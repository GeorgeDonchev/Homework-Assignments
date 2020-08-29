import re

pattern = r"^(\|([A-Z]{4,})\|:#(([A-Za-z])+( )[A-Za-z]+)#)$"

result = []
n = int(input())
for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if not matches == []:
        for match in matches:
            print(f"{match[1]}, The {match[2]}")
            print(f">> Strength: {len(match[1])}")
            print(f">> Armour: {len(match[2])}")
    else:
        print("Access denied!")


