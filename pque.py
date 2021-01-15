import math
t = int(input())
while t != 0:
    op = []
    n = input()
    l = list(map(int, input().split()))
    while sum(l) != 0:
        l.sort()
        op.append(max(l))
        l[l.index(max(l))] = math.floor(max(l) / 2)
    t -= 1
    print(*op)
# tle