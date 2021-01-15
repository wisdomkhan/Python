t = int(input())
op = []


def compare(a, b):
    if a > b:
        op.append('>')
    elif a < b:
        op.append('<')
    elif a == b:
        op.append('=')


for i in range(t):
    x, y = list(map(int, input().split()))
    compare(x, y)
for j in op:
    print(j)
