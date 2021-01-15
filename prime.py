op = []
for i in range(int(input())):
    n = int(input())
    c = 0
    for j in range(n):
        if n % (j + 1) == 0:
            c += 1
    if c == 2:
        op.append('yes')
    else:
        op.append('no')
for k in op:
    print(k)
