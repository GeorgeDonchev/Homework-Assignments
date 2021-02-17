phonebook = {}
is_finished = False
n = 0
while not is_finished:
    inputs = input()
    if inputs.isdigit():
        n = int(inputs)
        is_finished = True
        break
    name, phone_number =inputs.split("-")
    phonebook[name] = phone_number
if is_finished:
    for _ in range(n):
        name_to_search = input()
        if name_to_search in phonebook.keys():
            print(f"{name_to_search} -> {phonebook[name_to_search]}")
        else:
            print(f"Contact {name_to_search} does not exist.")