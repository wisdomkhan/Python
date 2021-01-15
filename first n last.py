t = int(input())
op = []


def sumFL(a):
    global f
    l = a % 10
    while a != 0:
        f = a
        a //= 10
    tot = f + l
    op.append(tot)


for i in range(t):
    n = int(input())
    sumFL(n)
for j in op:
    print(j)
