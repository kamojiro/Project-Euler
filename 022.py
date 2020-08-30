def namenumber( name):
    cnt = 0
    for x in name:
        cnt += ord(x) - ord('A') + 1
    return cnt
with open("./names.txt") as f:
    s = f.read()
    names = [ t.strip("\"") for t in s.split(",")]
ans = 0
names.sort()                              
print(names[937], namenumber(names[937])*938)
N = len(names)
for i in range(N):
    ans += namenumber( names[i])*(i+1)
print(ans)
