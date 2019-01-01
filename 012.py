from collections import defaultdict
def factor(D, n):
    for i in range(2, n+1):
        while n%i == 0:
            D[i] += 1
            n //= i
        if n == 1:
            return D
for i in range(2,100000):
    D = defaultdict( int)
    D = factor( factor(D, i), i+1)
    check = 1
    D[2] -= 1
    for x in D:
        check *= D[x] + 1
    if check >= 500:
        print( i*(i+1)//2)
        break
