inputs = input().split("|")
flatten_list = [print(j, end = " ") for i in reversed(inputs) for j in i.split() ]
