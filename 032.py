#import sys
#input = sys.stdin.readline
from itertools import permutations
from collections import defaultdict
def main():
    A = []
    for i in range(1,10):
        for P in permutations(range(1,10),r=i):
            A.append("".join( map( str, P)))
    N = len(A)
    print(N)
    print(A[:100])
    ans = 0
    P = list( map(str, range(1,10)))
    d = defaultdict( lambda : False)
    for i in range(N-1):
        a = A[i]
        la = len(a)
        if la > 3:
            break
        for j in range(i+1, N):
            b = A[j]
            lb = len(b)
            if la + lb > 9:
                break
            ab = str( int(a)*int(b))
            if la + lb + len(ab) != 9:
                continue
            abab = list( a)
            abab.extend( list(b))
            abab.extend( list(ab))
            abab.sort()
            if abab == P:
                print(a, b, ab)
                if d[ab]:
                    continue
                ans += int(ab)
                d[ab] = True
        print(a, ans)
    print(ans)
if __name__ == '__main__':
    main()
