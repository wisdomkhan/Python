T = int(input())
ans = []
while T != 0:
    n = int(input())
    ans.append(int(n ** 0.5))
    T -= 1
for i in ans:
    print(i)
