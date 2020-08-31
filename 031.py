#import sys
#input = sys.stdin.readline
def main():
    ans = 1
    for i in range(3):
        a = i*100
        for j in range(5):
            b = a+50*j
            if b > 200:
                break
            for k in range(11):
                c = b+20*k
                if c > 200:
                    break
                for l in range(21):
                    d = c+10*l
                    if d > 200:
                        break
                    for m in range(41):
                        e = d+5*m
                        if e > 200:
                            break
                        for n in range(101):
                            if e+n*2 <= 200:
                                ans += 1
                            else:
                                break
    print(ans)
                        
if __name__ == '__main__':
    main()
