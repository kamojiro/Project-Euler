#import sys
#input = sys.stdin.readline

def devide(x):
    ret = []
    N = 10**4
    t = 1
    for _ in range(N):
        t *= 10
        if t < x:
            ret.append(0)
            continue
        t, q = t%x, t//x
        ret.append(q)
        if t == 0:
            break
    return ret

def get_recurring(A):
    B = A[::-1]
    N = 10**4
    for i in range(1,N//2):
        if B[:i] == B[i:i*2]:
            return(i)
    return(1)


def main():
    ans = 0
    now = 7
    for i in range(2, 10**3):
        l = devide(i)
        if len(l) < 10**4:
            continue
        t = get_recurring(l)
        # print(i,l[:10], t)
        if t > ans:
            now = i
            ans = t
    print(now)

    
if __name__ == '__main__':
    main()
