#import sys
#input = sys.stdin.readline
def main():
    ans = 1
    now = 1
    N = 1001
    for i in range(N//2):
        for _ in range(4):
            now += i*2+2
            # print(now)
            ans += now
        # print(ans)
    print(ans)
if __name__ == '__main__':
    main()
