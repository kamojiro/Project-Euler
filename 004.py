def check(n):
    a = str(n)
    l = len(a)
    if a[:l//2][::-1] == a[l//2+l%2:]:
        return 1
    return 0
A = []
for i in range(1000):
    for j in range(1000):
        if check(i*j):
            A.append(i*j)
print( max(A))
