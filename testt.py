import re

pattern = r"([\=]|[\/])\b([A-Z][a-z]{2,})(\1)"
text = input()
t_points=0
valid_travels=[]
matches = re.findall(pattern, text)
if matches:
    for m in matches:
        t_points+=len(m[1])
        valid_travels.append(m[1])
    print(f"Destinations: {', '.join(valid_travels)}")
else:
    print(f'Destinations:')
print(f'Travel Points: {t_points}')
