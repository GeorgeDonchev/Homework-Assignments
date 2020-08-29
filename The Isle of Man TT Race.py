import re
is_valid = False
encrypted_message=""
racer_name=''
pattern = r"^(#|\$|%|&|\*)([A-Za-z]+)\1=(\d+)!!"
while True:
    text = input()
    get_geohash=text.split('!!', 1)
    if len(get_geohash) <= 1:
        print ('Nothing found!')
        continue
    geohash_code = get_geohash[1]
    matches = re.findall(pattern, text)
    text_length=0
    if matches:
        for match in matches:
            text_length = int(match[2])
            racer_name = match[1]
            if int(match[2]) == len(geohash_code):
                is_valid = True
                break
            else:
                print('Nothing found!')
                break
    else:
        print('Nothing found!')
    if is_valid:
        for t in geohash_code:
            encrypted_message+=chr(ord(t)+text_length)
        print(f"Coordinates found! {racer_name} -> {encrypted_message}")
        break

