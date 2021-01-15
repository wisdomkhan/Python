t = int(input())
op = []
for i in range(t):
    x, y, z = map(int, input().split())
    if x + y + z == 180:
        op.append('YES')
    else:
        op.append('NO')
for j in op:
    print(j)
