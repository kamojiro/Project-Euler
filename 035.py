#import sys
#input = sys.stdin.readline
def eratosthenes(N):
    from collections import deque
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    ret = []
    for i in range(N+1):
        if work[i]:
            ret.append(i)
            for j in range(2* i, N+1, i):
                work[j] = False
    return ret, work

def main():
    N = 10**6
    ans = 0
    primes, is_primes = eratosthenes(N)
    circular_primes = []
    for p in primes:
        t = len( str(p))
        x = p
        z = 10**(t-1)
        for _ in range(t-1):
            x = x//10+x%10*z
            if not is_primes[x]:
                break
        else:
            ans += 1
            circular_primes.append(p)
    print(ans)
    print(circular_primes)
        
    
    
if __name__ == '__main__':
    main()
