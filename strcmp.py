for _ in range(int(input())):
    s1,s2 = input().split()
    if s1 < s2:
        print(1)
    elif s2 < s1:
        print(2)
    elif s1 == s2:
        print(0)
