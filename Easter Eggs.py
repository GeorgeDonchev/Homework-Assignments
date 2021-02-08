def find_strongest_eggs(eggs, sublist_count):
    best_eggs = []
    for i in range(sublist_count):
        current_list =([eggs[idx] for idx in range (i, len (eggs), sublist_count)])

        midle_egg = current_list[len(current_list)//2]
        right_egg = current_list[len(current_list)//2 +1]
        left_egg = current_list[len(current_list)//2 -1]
        if left_egg < midle_egg > right_egg > left_egg:
            best_eggs.append(midle_egg)
    return best_eggs


print(find_strongest_eggs([-1, 7, 3, 15, 2, 12], 2))

print(find_strongest_eggs([51,21, 83, 15, 55], 1))

