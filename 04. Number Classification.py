numbers = [int(x) for x in input().split(", ")]
positive_numbers = [str(p) for p in numbers if p >=0]
print(f"Positive:", ', '.join(positive_numbers))
negative_numbers = [str(p) for p in numbers if p <0]
print(f"Negative:", ', '.join(negative_numbers))
even_numbers = [str(p) for p in numbers if p % 2==0]
print(f"Even:", ', '.join(even_numbers))
odd_numbers = [str(p) for p in numbers if p % 2 == 1]
print(f"Odd:", ', '.join(odd_numbers))