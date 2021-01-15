t = int(input())
op = []


def check(s):
    if len(s) % 2 == 0:
        if s[:len(s) // 2] in s[len(s) // 2:] or s[:len(s) // 2] in s[len(s) // 2:][::-1]:
            op.append('YES')
        else:
            op.append('NO')
    else:
        if s[:len(s) // 2] in s[len(s) // 2 + 1:] or s[:len(s) // 2] in s[len(s) // 2:][::-1]:
            op.append('YES')
        else:
            op.append('NO')


for x in range(t):
    st = input()
    check(st)
for y in op:
    print(y)
