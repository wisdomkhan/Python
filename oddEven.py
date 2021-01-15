t = int(input())
a = []

for _ in range(t):
    e = ''
    o = ''
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            e += str(i) + ' '
        else:
            o += str(i) + ' '
    print(o)
    print(e)
