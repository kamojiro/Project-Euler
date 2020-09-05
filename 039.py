#import sys
#input = sys.stdin.readline

def perimeter(x):
    cnt = 0
    for i in range(1,x):
        if x-i < i:
            break
        for j in range(i, x-i+1):
            k = x-i-j
            if k < j:
                break
            if i**2 + j**2 == k**2:
                # print(i,j,k)
                cnt += 1
    return cnt

def main():
    N = 1000
    # print(perimeter(120))
    ans = 3
    for i in range(12, N+1):
        cnt = perimeter(i)
        if cnt > ans:
            ans = cnt
            print(i, ans)
    print(ans)

if __name__ == '__main__':
    main()






