import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(input().rstrip()))
def bfs():
    q = [(0,0)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.pop(0)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or li[nx][ny] == '0': continue
            if li[nx][ny] == '1':
                li[nx][ny] = int(li[x][y]) + 1
                q.append((nx,ny))
bfs()
print(li[n-1][m-1])
    