import re

input_data = input()
pattern = r"^([A-Z][a-z]+([ ][a-z'\s]+)?):"
while not input_data == "end":
    matches = re.match(pattern, input_data)
    if matches:
        new_text=""
        key = int(len(matches[1]))
        for symbol in input_data:
            if symbol == ':':
                new_text+="@"
                continue
            if not symbol == ' ' or not symbol == "\'":
                if 64<ord(symbol)<91 and ord(symbol)+key > 90:
                    symbol=chr(65 + (ord(symbol)+key)-90)
                elif 96<ord(symbol)<123 and ord(symbol)+key > 122:
                    symbol=chr(97 + (ord(symbol)+key)-122)
                else:
                    new_text+=chr(ord(symbol)+key)
            else:
                if symbol == ' ':
                    new_text+=' '
                elif symbol == "\'":
                    new_text+="\'"
        print(f"Successful encryption: {new_text}")
    else:
        print("Invalid input!")
    input_data = input()