#import sys
#input = sys.stdin.readline
def is_pandigital(x):
    digits = [False]*10
    cnt = 0
    y = x
    ret = ""
    while True:
        cnt += len( str(y))
        ret += str(y)
        if cnt > 9:
            return 0
        for t in map( int, list( str(y))):
            if t == 0:
                return 0
            if digits[t]:
                return 0
            else:
                digits[t] = True
        if cnt == 9:
            break
        y += x
    return int(ret)

def main():
    N = 10**6
    ans = 0
    for i in range(3,N):
        t = is_pandigital(i)
        if ans < t:
            ans = t
    print(ans)
if __name__ == '__main__':
    main()
