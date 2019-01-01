from collections import defaultdict
D = defaultdict( int)
E = defaultdict( int)
D[1] = D[2] = D[6] = D[10] = 3
D[4] = D[5] = D[9] = 4
D[3] = D[7] = D[8] = D[40] = D[50] = 5
D[11] = D[12] = D[20] = D[30] = D[80] = 6
D[15] = D[16] = 7
D[13] = D[14] = D[18] = D[19] = 8
D[17] = 9
for i in range(2,10):
    for j in range(10):
        if j == 0 and i != 2 and i != 3 and i != 8 and i != 4 and i != 5:
            D[i*10] = D[i] + 2
        else:
            D[i*10 + j] = D[i*10] + D[j]
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if j == 0 and k == 0:
                D[100*i] = D[i]+7
            elif j == 0:
                D[i*100+k] = D[i] + 10 + D[k]
            else:
                D[i*100 + 10*j + k] = D[i] + 10 + D[10*j+k]
D[1000] = 11
ans = 0
for i in range(1,1001):
    print(i,D[i])
    ans += D[i]
print( ans)
for i in range(1,10):
    print(i,D[111*i])
print(D[55])







