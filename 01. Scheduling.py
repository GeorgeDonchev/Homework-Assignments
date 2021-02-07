from collections import deque

jobs = list(map(int, input().split(", ")))
jobs_as_list = list(jobs)

index = int(input())
cycles = 0
needed_num = jobs[index]
jobs = sorted(jobs)
# print(jobs)

for n in range(len(jobs)):
    cycles+=jobs[n]
    if needed_num == jobs[n]:
        if n<len(jobs)-1:
            if jobs[n+1]!=needed_num:
                print(cycles)
                break

