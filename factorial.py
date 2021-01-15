t = int(input())
zeros = []


def c_zeros(k):
    c = 0
    while k % 10 == 0:
        c += 1
        k //= 10
    zeros.append(c)
    print(c)


def factorial(a):
    f = 1
    while a != 0:
        f *= a
        a -= 1
    c_zeros(f)


for i in range(t):
    n = int(input())
    factorial(n)
for j in zeros:
    print(j)
# tle