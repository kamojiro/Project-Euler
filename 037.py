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
    return work

def is_truncatable(x, primes):
    y = x
    digits = []
    while y > 0:
        # print(y)
        if not primes[y]:
            return False
        digits.append(y%10)
        y //= 10
        
    num = 0
    for i, digit in enumerate(digits):
        num += digit*10**i
        # print(num)
        if not primes[num]:
            return False
    return True

def main():
    N = 10**6
    primes = eratosthenes(N)
    ans = 0
    num = 0
    for i in range(11, N+1):
        if is_truncatable(i, primes):
            num += 1
            ans += i
            print(num, i)
        if num > 11:
            break
    # print(is_truncatable(3797, primes))
    print(ans)
if __name__ == '__main__':
    main()
