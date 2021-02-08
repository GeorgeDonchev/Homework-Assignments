def numbers_searching(*args):
    sorted_numbers = sorted(args)
    occurences= set()
    for number in sorted_numbers:
        if sorted_numbers.count(number) > 1:
            occurences.add(number)
    min_num = min(sorted_numbers)
    max_num = max(sorted_numbers)
    missing_num =None
    for m in range(min_num, max_num):
        if m not in sorted_numbers:
            missing_num = m
            break
    final_output =[missing_num, sorted(occurences)]
    return final_output


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))