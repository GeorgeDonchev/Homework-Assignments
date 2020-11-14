from collections import deque

inputs = input()
half_inputs = len (inputs) // 2
first_half = []
second_half = deque ()
is_balanced = True

for e in range (half_inputs):
    if inputs[e] == "(" or inputs[e] == "{" or inputs[e] == "[":
        first_half.append(inputs[e])
    else:
        is_balanced = False
        break

for e in range (half_inputs, len(inputs)):
    if inputs[e] == ")" or inputs[e] == "}" or inputs[e] == "]":
        second_half.append(inputs[e])
    else:
        is_balanced = False
        break

while first_half and second_half:
    if not 0 < ord(second_half.popleft()) - ord(first_half.pop()) <=2:
        is_balanced = False
if is_balanced:
    print("YES")
else:
    print("NO")

