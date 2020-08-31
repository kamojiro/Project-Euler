#import sys
#input = sys.stdin.readline
def is_sum_of_fifth_powers(x):
    return x == sum( map( lambda x:int(x)**5, list( str(x))))

def main():
    N = 10**6
    ans = 0
    for i in range(2, N):
        if is_sum_of_fifth_powers(i):
            ans += i
    print(ans)
if __name__ == '__main__':
    main()
