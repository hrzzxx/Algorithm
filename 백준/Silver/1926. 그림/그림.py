import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1,1,0,0], [0,0,-1,1]
q = deque([])

res = [0,0]
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            res[0] += 1
            q.append((i,j))
            cnt = 0
            while q:
                x,y = q.popleft()
                if not maps[x][y]: continue
                maps[x][y] = 0
                cnt += 1

                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<n and 0<=ny<m and maps[nx][ny]:
                        q.append((nx,ny))
            res[1] = max(res[1], cnt)
print(*res, sep='\n')