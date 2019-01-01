ans = 0
for i in range(1,999):
    for j in range(i+1,1000):
        if i**2 + j**2 == (1000-i-j)**2:
                ans = i*j*(1000-i-j)
                break
    if ans > 0:
        break
print( ans)






