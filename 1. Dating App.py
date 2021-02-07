from collections import deque
males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0
while males and females:
    current_f = females.popleft()
    current_m = males.pop()
    if current_m<=0:
        females.appendleft(current_f)
    elif current_f <=0:
        females.popleft()
    elif current_m % 25 == 0 and len(males)>0:
        males.pop()
        females.appendleft(current_f)
    elif current_f % 25 == 0 and len(females)>0:
        females.popleft()
        males.append(current_m)
    elif current_f == current_m:
        matches+=1
    else:
        males.append(current_m-2)

print(f'Matches: {matches}')
print(f'Males left: {"none" if len(males)==0 else ", ".join(map(str, males[::-1]))}')
print(f'Females left: {"none" if len(females)==0 else ", ".join(map(str, females))}')