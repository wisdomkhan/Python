op = []
ns = ''
s = ''

while int(input()) != 0:
    ns = ''
    s = ''
    l = list(map(int, input().split()))  # list of integers of permutation
    ans = [] * 10
    for i in range(len(l)):
        s += str(l[i])
        ans.insert(l[i], i + 1)
    for j in ans:
        ns += str(j)
    if ns == s:
        print(ns, ' ', s)
        op.append('Ambiguous')
    else:
        print(ns, ' ', s)
        op.append('not ambiguous')
for x in op:
    print(x)
