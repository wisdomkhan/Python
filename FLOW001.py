T = int(input())
op = []
if T >= 1 <= 1000:  # cons 1
    for i in range(T):
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a >= 0 <= 10000 and b >= 0 <= 10000:  # cons 2
            op.append(a + b)
        else:
            quit()
    for j in op:
        print(j)
else:
    quit()
