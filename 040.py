#import sys
#input = sys.stdin.readline
def main():
    ans = 1
    cnt = 0
    N = 10**6
    C = 1
    for i in range(1,N):
        t = len(str(i))
        if cnt+t >= C:
            ans *= int(str(i)[C-cnt-1])
            C *= 10
            if C == 10000000:
                break
        cnt += t
    print(ans)
if __name__ == '__main__':
    main()







