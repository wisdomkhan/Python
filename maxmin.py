c = 0
op = []
t = int(input())
for x in range(t):
    n = int(input())
    l = list(map(int, input().split()[:n]))
    if len(l) == 1:
        op.append(l[0])
    else:
        for i in range(len(l) - 1):
            c += min(l[i], l[i + 1])
            if l[i] < l[i + 1]:
                t = l[i]
                l[i] = l[i + 1]
                l[i + 1] = t
        op.append(c)
        c = 0
for y in op:
    print(y)
