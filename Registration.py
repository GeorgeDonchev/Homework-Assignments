import re
count=0
n =int(input())
pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([a-z]{5,}[0-9]+)P@\$"
for _ in range(n):
    registration = input()
    matches = re.findall(pattern, registration)

    if not matches:
        print("Invalid username or password")
    else:
        count+=1
        print("Registration was successful")
        for match in matches:
            print(f"Username: {match[0]}, Password: {match[1]}")
print(f"Successful registrations: {count}")