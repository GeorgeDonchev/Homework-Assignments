import re
n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
digit_pattern = r"\d+"
for n in range(n):
    barcode = input()
    matches = re.findall(pattern, barcode)

    if not matches:
        print("Invalid barcode")
        continue
    digit_match = re.findall(digit_pattern, barcode)
    if not digit_match:
        print(f"Product group: 00")
    else:
        print(f"Product group: {''.join(digit_match)}")
