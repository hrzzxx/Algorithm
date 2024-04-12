import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(r)]

h,w = r,0
dx,dy = [-1,1,0,0], [0,0,-1,1]
res = 0
def dfs(x,y,cnt):
    global res
    if (x,y) == (0,c-1) and cnt == k: 
        # print(*maps,sep='\n')
        # print(cnt)
        res += 1
        return res
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx < r and 0<= ny < c and maps[nx][ny] == '.':
            maps[nx][ny] = cnt
            dfs(nx,ny,cnt+1)
            maps[nx][ny] = '.'
        else:
            continue
dfs(h,w,0)
print(res)
