t = int(input())
c1 = 0
c2 = 0
Alead = []
lead = []


def score(a, b):
    global c1
    global c2
    c1 += int(a)
    c2 += int(b)
    Alead.append(abs(c1 - c2))
    lead.append(c1 - c2)


for _ in range(t):
    x, y = input().split()
    score(x, y)
m = max(Alead)
if lead[Alead.index(m)] > 0:
    print(1, ' ', m)
else:
    print(2, ' ', m)
