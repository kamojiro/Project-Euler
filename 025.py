#import sys
#input = sys.stdin.readline
def main():
    cnt = 3
    f1 = 1
    f2 = 1
    for _ in range(10000):
        f1, f2 = f2, f1+f2
        if len( str(f2)) >= 1000:
            print(cnt)
            break
        cnt += 1
if __name__ == '__main__':
    main()
