#import sys
#input = sys.stdin.readline
from itertools import permutations

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int( x**(1/2))+1):
        if x%i == 0:
            return False
    return True

def main():
    ans = 0
    for p in permutations( range(1,8)):
        t = int("".join( map( str, p)))
        print(t)
        if is_prime(t):
            ans = t
    print(ans)
    
if __name__ == '__main__':
    main()
