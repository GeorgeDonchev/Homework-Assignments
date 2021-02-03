import operations
num1, sign, num2 = input().split()
res = operations.op(float(num1), int(num2), sign)
print(f"{res:.2f}")