inputs = input().split(", ")
n = int(input())
items = {category: {} for category in inputs}
print(items)
for _ in range(n):
    commands = input().split(" - ")
    category = commands[0]
    substance = commands[1]
    values = commands[2].split(';')
    qty = int(values[0].split(":")[1])
    quality = int(values[1].split(":")[1])

    if category in items:
        items[category][substance] = [qty, quality]

qty_items = [items[k][y][0]for k in items for y in items[k]]
quality_items = [items[k][v][1] for k in items for v in items[k]]
print(f"Count of items: {sum(qty_items)}")
print(f"Average quality: {(sum(quality_items)/len(items)):.2f}")
[print(f"{k} -> {', '.join(v)}")for k, v in items.items()]