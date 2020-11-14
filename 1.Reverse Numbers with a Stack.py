inputs = input().split(" ")
reversed_inputs=[]
while inputs:
    current_digit=inputs.pop()
    reversed_inputs.append(current_digit)

print(' '.join(reversed_inputs))