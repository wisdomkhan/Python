t = int(input())
op = []


def notes(a):
    ans = 0
    j = 0
    d = [100, 50, 10, 5, 2, 1]
    while a > 0:
        ans += a // d[j]
        a %= d[j]
        j += 1
    op.append(ans)


for i in range(t):
    m = int(input())
    notes(m)
for k in op:
    print(k)
