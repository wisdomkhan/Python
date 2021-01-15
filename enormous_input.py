l = []


def divisible(v):
    c = 0
    for j in v:
        if j % int(k) == 0:
            c += 1
    return c


n, k = input().split()
if int(n) <= 10 ** 7 > 0 and int(k) <= 10 ** 7 > 0:
    for i in range(int(n)):
        x = int(input())
        if x > 0 <= 10 ^ 9:
            l.append(x)
    print(divisible(l))
