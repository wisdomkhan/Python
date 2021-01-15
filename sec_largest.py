T = int(input())
l = []
op = []


def sec_largest(lt):
    m = max(lt)
    l.remove(m)
    op.append(max(l))
    l.clear()


for i in range(T):
    x, y, z = list(map(int, input().split()))
    l.append(x)
    l.append(y)
    l.append(z)
    sec_largest(l)
for j in op:
    print(j)
