n = int(input())
c = 0
count = {}
l = list(map(int, input().split()))
for i in l:
    count[i] = count.get(i, 0) + 1
for v in count.values():
    while v > 1:
        v -= 1
        c += 1
print(c)
