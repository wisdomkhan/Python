t = int(input())
op = []


def count_four(st):
    four = 0
    for i in range(len(st)):
        if s[i] == '4':
            four += 1
    return four


while t != 0:
    s = input()
    op.append(count_four(s))
    t -= 1
for j in op:
    print(j)
