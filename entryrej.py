n = int(input())
check = []
op = []
for i in range(n):
    e = input()
    if e in check:
        op.append("YES")
        check.append(e)
    else:
        op.append("NO")
        check.append(e)
for j in op:
    print(j)
