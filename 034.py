#import sys
#input = sys.stdin.readline
def main():
    N = 10**7
    T = [1]*10
    for i in range(1,10):
        T[i] = T[i-1]*i

    ans = 0
    for x in range(3,N):
        if x == sum( map( lambda x: T[int(x)], list( str(x)))):
            ans += x
    print(ans)
if __name__ == '__main__':
    main()
