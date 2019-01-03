def d(n):
    wa = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            wa += i
    return wa
ans = 0
print(d(220), d(284), d(d(220))) 
for i in range(1,10001):
    a = d(i)
    if a != i and d(a) == i:
        ans += i
print(ans)
