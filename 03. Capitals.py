countries = input().split(", ")
capitals = input().split(", ")
combinated = {print(f"{c} -> {s}") for c, s in zip(countries, capitals)}
