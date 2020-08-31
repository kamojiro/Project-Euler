#import sys
#input = sys.stdin.readline
def main():
    A = set()
    for a in range(2,101):
        t = a*a
        for _ in range(2,101):
            A.add(t)
            t *= a
    print(len(A))
if __name__ == '__main__':
    main()
