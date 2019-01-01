# primes = []
# n = 0
# m = 2
# while n < 10001:
#     for _,p in primes:
#         if p > int( n**(1/2))+1:
#             primes.append((n,m))
#             n += 1
#             break
#         if m%p == 0:
#             break
#     else:
#         primes.append((n,m))
#         n += 1
#     m += 1
n = 1
for i in range(2,10**6):
    prime = 1
    for j in range(2,int(i**(1/2))+1):
        if i%j == 0:
            prime = 0
            break
    if prime:
        if n == 10001:
            p = i
            break
        n+= 1
        
print(p)
