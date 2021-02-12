s = int(input())
students = {}
for _ in range(s):
    args = input().split()
    student = args[0]
    mark = float(args[1])
    if student not in students:
        students[student] = []
    students[student].append(mark)

for key, value in students.items():
    avg = sum(value)/len(value)
    value = ["{:.2f}".format(x) for x in value]
    print(f"{key} -> { ' '.join(value)} (avg: {avg:.2f})")

