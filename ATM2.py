T = int(input())
op = []


def check(l):
    global K
    K = int(K)
    s = ''
    for j in l:
        if j <= K:
            s += '1'
            K = K - j
        else:
            s += '0'
    return s


if T >= 1 <= 100:  # con 1
    for i in range(T):
        global A
        N, K = input().split()
        if int(N) >= 1 <= 100 and int(K) >= 1 <= 1000000:  # con 2, 4
            A = list(map(int, input().split()[:int(N)]))  # inputting N As
            op.append(check(A))
        else:
            quit('A nir')
        for m in A:
            if m >= 1 <= 1000000:  # con 3
                continue
            else:
                quit('Ai nir')
else:
    quit('T nir')
for k in op:
    print(k)
