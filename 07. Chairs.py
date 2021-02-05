def find_pairs(people, group, res=[]):
    i = 0
    if len(res) == group:
        print(', '.join(res))
        return
    for i in range(len(people)):
        x = people[i]
        res.append(x)
        find_pairs(people[i+1:], group, res)
        res.pop()

people = list(input().split(", "))
group = int(input())
find_pairs(people, group)