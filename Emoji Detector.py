import re

text = input()
threshold_value=1
threshold_pattern = r"\d"
threshold_matches = re.findall(threshold_pattern, text)
for cool_threshold in threshold_matches:
    threshold_value*=int(cool_threshold)
print(f"Cool threshold: {threshold_value}")

emoji_pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
emoji_matches=re.findall(emoji_pattern, text)

if emoji_matches:
    print (f"{len (emoji_matches)} emojis found in the text. The cool ones are:")
    for match in emoji_matches:
        level=0
        for e in match[1]:
            level+=ord(e)
        if level >= threshold_value:
            print(''.join(match))
