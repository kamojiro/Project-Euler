#import sys
#input = sys.stdin.readline

def is_prime(x):
    x = abs(x)
    y = x
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        while x%i == 0:
            x //= i
    if y > x:
        return False
    else:
        return True

def consective_primes(a,b):
    for i in range(1000):
        if is_prime(i**2 + a*i + b):
            continue
        return i+1

def main():
    ans = 0
    l = 0
    # for i in range(10):
    #     print(i, is_prime(i))
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            t = consective_primes(a,b)
            if l < t:
                l = t
                ans = a*b
    print(ans)
if __name__ == '__main__':
    main()
