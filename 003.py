from heapq import *
N = 600851475143
q = []
for i in range(2,N):
    while N%i == 0:
        N //= i
        print(i, N)










