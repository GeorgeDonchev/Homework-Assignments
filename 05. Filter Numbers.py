start_num = int(input())
end_num = int(input())
divisibles = [num for num in range(2, 11)]
list_of_digits = [digit for digit in range(start_num, end_num+1) if any(digit % x == 0 for x in divisibles)]
print(list_of_digits)