#import sys
#input = sys.stdin.readline

def sumOfProperDivisors(n):
    if n == 1:
        return 0
    ret = 1
    m = n
    for i in range(2, int(n**(1/2))+1):
        cnt = 1
        while m%i == 0:
            m //= i
            cnt = cnt*i+1
#        print(n,i,cnt)
        ret *= cnt
#    print(m)
    if m > 1:
        ret *= 1+m
    
    return ret - n
def main():
    N = 28213
    ans = 0
    abundants = [False]*(N+1)
#    N = 10
    for i in range(1,N+1):
#        print("sum", i, sumOfProperDivisors(i))
        if sumOfProperDivisors(i) > i:
            abundants[i] = True
            
    ans += 1
    for i in range(2, N+1):
        for j in range(1, i//2+1):
            if abundants[j] and abundants[i-j]:
                ans -= i
                break
    ans += i
    print(ans)
if __name__ == '__main__':
    main()
