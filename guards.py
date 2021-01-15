t = int(input())
op = {}
for i in range(t):
    a, b = input().split()
    op[max(int(a), int(b))] = int(a) + int(b)
for k, v in op.items():
    print(k, ' ', v)
