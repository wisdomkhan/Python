n, q = input().split()
ps = []
ps.append(0)
L = list(map(int, input().split()))
for i in range(len(L)):
    s = 0
    for j in range(i+1):
        s += L[j]
    ps.append(s)
for i in range(int(q)):
    l, r = input().split()
    print(ps[int(r)] - ps[int(l)-1])
# tle