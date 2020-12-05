text = input()
the_vowels = ['a', 'o', 'u', 'e', 'i']
new_text = [char for char in text if char.lower() not in the_vowels]
print("".join(new_text))