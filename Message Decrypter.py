import re

pattern = r"^([$|%])([A-Z][a-z]{2,})\1: (\[(\d+)\])\|(\[(\d+)\])\|(\[(\d+)\])\|$"
elements =[]
n = int(input())
for _ in range(n):
    text = input()
    matches = re.findall(pattern, text)
    if matches:
        string = ""
        for match in matches:
            currant_tag = match[1]
            string=chr(int(match[3]))+chr(int(match[5]))+chr(int(match[7]))
        print(f'{currant_tag}: {string}')
    else:
        print("Valid message not found!")

