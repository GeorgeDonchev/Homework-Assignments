from collections import deque
n = int(input())
final_sequence = deque()
for _ in range(n):
    inputs = list(map(int, input().split()))
    rule = inputs[0]
    if rule == 1:
        digit = inputs[1]
        final_sequence.append(digit)
    elif rule == 2:
        if final_sequence:
            final_sequence.popleft()
    elif rule == 3:
        print(max(final_sequence))
    elif rule == 4:
        print(min(final_sequence))
final_sequence = deque(map(str, final_sequence))
print(", ".join(final_sequence))