#import sys
#input = sys.stdin.readline
def is_palindromic(n):
    y = str(n)
    for i in range( len(y)//2):
        if y[i] != y[-i-1]:
            return False
    x = bin(n)[2:]
    for i in range( len(x)//2):
        if x[i] != x[-i-1]:
            return False
    return True

def main():
    ans = 0
    N = 10**6
    print([(bin(i), is_palindromic(i)) for i in range(1,11)])
    for i in range(1, N):
        if is_palindromic(i):
            ans += i
    print(ans)
        
if __name__ == '__main__':
    main()
