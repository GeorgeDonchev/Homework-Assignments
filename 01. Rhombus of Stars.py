def print_line(n):
    for i in range(0, n):
        print((n-i-1)*" " + (n)*" * " + (n-i-1)*" ")


size = int(input())
for n in range(1, size+1):
    print_line(n)
for n in range(size-1, 0, -1):
    print_line(n)

