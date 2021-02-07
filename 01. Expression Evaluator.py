def find_first_opr(string):
    for element in string_expression:
        if element in list_of_opr:
            return element


string_expression =input()
list_of_opr = ["+","-", "*", "/"]
first_opr = find_first_opr(string_expression)
final_result =""
for el in string_expression:
    current_result = None
    args = string_expression.split(first_opr)
    num_1, num_2 = args[0].split()
    current_result = eval(num_1+first_opr+num_2)
    final_result = str(current_result)




