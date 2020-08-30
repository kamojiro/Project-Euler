#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    A = list( permutations( range(10)))
    print("".join( map( str, A[10**6-1])))
    
if __name__ == '__main__':
    main()
