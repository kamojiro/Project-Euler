from collections import defaultdict
D = defaultdict( lambda : -1)
D[1] = 0
A = [(0,0)]*(10**6)
anschain = 0
ans = 1
for i in range(2,10**6):
    n = i
    m = 0
    while n != 1:
        m += 1
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        if not D[n] == -1:
            m += D[n]
            break
    if anschain < m:
        ans = i
        anschain = m
print(ans)

