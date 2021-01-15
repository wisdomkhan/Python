t = int(input())
while t > 0:
    d, n = input().split()
    d = int(d)
    n = int(n)
    s = 0
    for i in range(d):
        s = n * (n + 1) // 2
        n = s
    print(s)
    t -= 1
