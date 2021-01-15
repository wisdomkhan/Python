p = 10**9 + 7
for _ in range(int(input())):
    ans = 0
    e = 3
    n = int(input())
    while e != 0:
        ans += n**e
        e -= 1
    print(int(ans%p))
