import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(m)]

dx,dy = [-1,1,0,0], [0,0,-1,1]
def dfs(x,y,cnt,color):
    maps[x][y] = cnt
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx < m and 0<= ny < n and maps[nx][ny] == color:
                cnt = dfs(nx,ny,cnt+1,color)
    return cnt
res = [0,0]
for i in range(m):
    for j in range(n):
        if maps[i][j] == 'W':
            res[0] += dfs(i,j,1,'W')**2
        elif maps[i][j] == 'B':
            res[1] += dfs(i,j,1,'B')**2
print(*res)