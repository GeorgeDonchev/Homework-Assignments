from collections import deque

boxes_of_materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))
present_materials = {150 : 'Doll', 250 : "Wooden train", 300 : 'Teddy bear', 400 : 'Bicycle'}
crafted_present = {'Doll': 0, "Wooden train": 0, 'Teddy bear': 0, 'Bicycle': 0}
succeeded_craft_present = 0
while boxes_of_materials and magic_levels:
    current_box = boxes_of_materials.pop()
    current_magic_level = magic_levels.popleft()
    magic_level = current_box*current_magic_level
    if magic_level < 0:
        boxes_of_materials.append(current_magic_level+current_box)
    elif magic_level > 0 and magic_level not in present_materials:
        boxes_of_materials.append(current_box+15)
    elif current_box == 0 or current_magic_level == 0:
        if current_box>0:
            boxes_of_materials.append(current_box)
        if current_magic_level > 0:
            magic_levels.appendleft(current_magic_level)
        continue
    elif magic_level in present_materials:
        present = present_materials[magic_level]
        crafted_present[present] +=1
if (crafted_present['Doll'] > 0 and crafted_present['Wooden train'] > 0) or (crafted_present['Teddy bear'] >0 and crafted_present['Bicycle']> 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print('No presents this Christmas!')

if boxes_of_materials:
    print(f'Materials left: {", ".join(map(str, boxes_of_materials[::-1]))}')
if magic_levels:
    print(f'Materials left: {", ".join(map(str, magic_levels[::-1]))}')
for key, values in sorted(crafted_present.items(), key = lambda x: x[0]):
    if crafted_present[key] > 0:
        print(f'{key}: {values}')