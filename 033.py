#import sys
#input = sys.stdin.readline
def main():
    numerator = 1
    denominator = 1
    for i in range(10,99):
        for j in range(i+1,100):
            if i%10 == 0 and j%10 == 0:
                continue
            i0, i1 = map( int, list( str(i)))
            j0, j1 = map( int, list( str(j)))
            if i0 == i1 or j0 == j1:
                continue
            if i0 == j0:
                i0, j0 = i1, j1
            elif i0 == j1:
                i0, j0 = i1, j0
            elif i1 == j0:
                i0, j0 = i0, j1
            elif i1 == j1:
                i0, j0 = i1, j1
            else:
                continue
            if i*j0 == i0*j:
                numerator *= i0
                denominator *= j0
                print(i,j,i0, j0)
    print(numerator, denominator)
if __name__ == '__main__':
    main()
