import re

pattern = r"(\*|@)([A-Z][a-z]{2,})(\1): \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|( ?)$"

n = int(input())
for _ in range(n):
    text = input()
    matches = re.findall(pattern,text)
    if not matches:
        print("Valid message not found!")
    else:
        for match in matches:
            print(f"{match[1]}: {ord(match[3])} {ord(match[4])} {ord(match[5])}")
