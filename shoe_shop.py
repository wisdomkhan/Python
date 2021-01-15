money = 0
d = {}
needs = []
X = int(input())  # no of shoes
if X >= 1 <= 10 ^ 3:  # con 1
    sizes = list(map(int, input().split()[:X]))
    N = int(input())  # no of customers
    if N > 0 <= 10 ^ 3:  # con 2
        for p in range(N):
            d = dict(input().split())  # taking demand as a dict and storing it in cm
            for a in d.values():
                if int(a) > 20 < 100:  # con 3
                    for b in d.keys():
                        if int(b) > 2 < 20:  # con 4
                            needs.append(d)
                else:
                    quit()

    for i in needs:  # checking for size, if present add value to money and del size
        for k in i.keys():
            if k in d:
                for v in i.values():
                    money += v
                    sizes.remove(k)
    else:
        quit()
    print("Money = ", money)
else:
    quit()
