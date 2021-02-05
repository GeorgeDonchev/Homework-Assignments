numbers = [i for i in map(int, input().split())]
negative_numbers = filter(lambda x: x < 0, numbers)
positive_numbers = filter(lambda y: y >= 0, numbers)
sum_of_negative_numbers = sum(negative_numbers)
sum_of_positive_numbers = sum(positive_numbers)
print(sum_of_negative_numbers)
print(sum_of_positive_numbers)
if sum_of_positive_numbers > abs(sum_of_negative_numbers):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")