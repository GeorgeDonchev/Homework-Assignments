import re

pattern = r"^(\S+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|(\S[^<>]{2})<(\1)"
n = int(input())

for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if not matches:
        print("Try another password!")
        continue
    for match in matches:
        print(f"Password: {match[1]}{match[2]}{match[3]}{match[4]}")