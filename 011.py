def prod(G, x, y):
    ans = 0
    if y >= 3:
        ans = max( ans, G[x][y-3]*G[x][y-2]*G[x][y-1]*G[x][y])
    if y <= 16:
        ans = max( ans, G[x][y+3]*G[x][y+2]*G[x][y+1]*G[x][y])
    if x >= 3:
        ans = max( ans, G[x-3][y]*G[x-2][y]*G[x-1][y]*G[x][y])
    if x <=  16:
        ans = max( ans, G[x+3][y]*G[x+2][y]*G[x+1][y]*G[x][y])
    if x >= 3 and y >= 3:
        ans = max( ans, G[x-3][y-3] * G[x-2][y-2] * G[x-1][y-1] * G[x][y])
    if x >= 3 and y <= 16:
        ans = max( ans, G[x-3][y+3] * G[x-2][y+2] * G[x-1][y+1] * G[x][y])
    if x <= 16 and y >= 3:
        ans = max( ans, G[x+3][y-3] * G[x+2][y-2] * G[x+1][y-1] * G[x][y])
    if x <= 16 and y <= 16:
        ans = max( ans, G[x+3][y+3] * G[x+2][y+2] * G[x+1][y+1] * G[x][y])
    return ans
G = [ list( map( int, input().split())) for _ in range(20)]
ans = 0
for i in range(20):
    for j in range(20):
        ans = max( ans, prod(G, i,j))
print(ans)
