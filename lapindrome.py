t = int(input())
c = []


def check(s):
    x = len(s) // 2
    for i in range(x):
        if len(s) % 2 == 0:
            if s.count(s[i], 0, x) == s.count(s[i], x, len(s)):
                c.append(1)
            else:
                c.append(0)
        else:
            if s.count(s[i], 0, x) == s.count(s[i], x + 1, len(s)):
                c.append(1)
            else:
                c.append(0)
    if c.count(0) == 0:
        print('YES')
    else:
        print('NO')
    c.clear()


for _ in range(t):
    st = input()
    check(st)
