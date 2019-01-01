ans = 0
for i in range(2, 2*10**6):
    for j in range( 2, int(i**(1/2))+1):
        if i%j == 0:
            t = 1
            break
    else:
        ans += i
print(ans)
