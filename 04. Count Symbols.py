text = list(map(str, input()))
set_chars = set([x for x in text])

for char in sorted(set_chars):
    print (f"{char}: {text.count (char)} time/s")

