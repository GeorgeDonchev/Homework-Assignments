from collections import deque
text = input().split()
main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange':('red', 'yellow'), 'purple':('red', 'blue'), 'green':('yellow', 'blue')}
made_colors = []

while text:
    first_element = text.pop(0)
    last_element = ''
    if len(text)>=1:
        last_element = text.pop()
    first_combination = first_element + last_element
    second_combination = last_element + first_element
    if first_combination in main_colors or first_combination in secondary_colors:
        made_colors.append(first_combination)
    elif second_combination in main_colors or second_combination in secondary_colors:
        made_colors.append(second_combination)
    else:
        if len(first_element)>1:
            text.insert(len(text)//2, first_element[:-1])
        if len(last_element)>1:
            text.insert (len (text) // 2, last_element[:-1])

for i in range(len(made_colors)-1, -1, -1):
    current_c = made_colors[i]
    if current_c in secondary_colors and any(x not in made_colors for x in secondary_colors[current_c]):
        made_colors.remove(current_c)
print(made_colors)
