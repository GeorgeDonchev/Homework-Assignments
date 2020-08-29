import re

n = int(input())
pattern = r"!([A-Z][A-Za-z]{3,})!:\[([A-Za-z]{8,})\]"

for _ in range (n):
    text = input()
    matches = re.findall(pattern, text)
    if matches == []:
        print("The message is invalid")
    else:
        for m in matches:
            print(f"{m[0]}:", end=" ")
            for symbol in m[1]:
                print(f"{ord(symbol)}", end = " ")
        print()
