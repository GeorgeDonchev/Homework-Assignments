def func_executor(*args):
    res = []
    for elements in args:
        func = elements[0]
        param = elements[1]
        res.append(func(*param))
    return res


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
