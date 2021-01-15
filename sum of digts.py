T = int(input())
s = []


def add(n):
    add_all = 0
    while n != 0:
        d = n % 10
        add_all += d
        n = int(n / 10)
    return add_all


if T >= 1 <= 1000:
    for i in range(T):
        N = int(input())
        if N >= 1 <= 1000000:
            s.append(add(N))
        else:
            quit()
    for j in s:
        print(j)
else:
    quit()
