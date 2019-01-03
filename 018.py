from copy import deepcopy
T = [ list( map( int, input().split())) for i in range(15)]
A = [(T[0][0],0)]
for i in range(1,15):
    B = deepcopy(A)
    A = []
    for x, d in B:
        A.append((x+T[i][d], d))
        A.append((x+T[i][d+1], d+1))
print( max(A))
        
