commands = input ()
bands_members = {}
bands_time = {}
while not commands == "start of concert":
    tokens = commands.split('; ')
    command = tokens[0]
    band_name = tokens[1]
    items = tokens[2]
    if command == "Add":
        members = items.split(', ')
        if band_name not in bands_members:
            bands_members[band_name] = []
            # bands_time[band_name] = 0
        for m in members:
            if m not in bands_members[band_name]:
                bands_members[band_name].append(m)

    elif command == "Play":
        time = int(items)
        if band_name not in bands_time:
            bands_time[band_name] = time
            # bands_members[band_name] = []
        else:
            bands_time[band_name]+=time
    commands = input ()

while True:
    final_band = input()
    if final_band in bands_members:
        break
total_time=0
for times in bands_time.values():
    total_time+=times
print(f"Total time: {total_time}")
for k, v in sorted(bands_time.items(), key = lambda t: (-t[1], t[0])):
    print(f"{k} -> {v}")
print(final_band)
for values in bands_members[band_name]:
    print(f"=> {values}")