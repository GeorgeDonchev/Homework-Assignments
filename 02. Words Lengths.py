strings = input().split(", ")
l_and_s = [print(f"{s} -> {len(s)}", end=", ") if not s == strings[-1] else print(f"{s} -> {len(s)}", end="") for s in strings]