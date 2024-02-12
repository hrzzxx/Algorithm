import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    n, m = map(int, input().split())
    if (n,m) == (0,0): break
    maps = [list(map(int, input().split())) for _ in range(m)]
    dx, dy = [0,0,-1,1,-1,1,-1,1], [1,-1,0,0,1,1,-1,-1]

    def search(x, y, cnt):
        if x>=n or x < 0 or y >= m or y < 0 or maps[y][x]!=1: return 0

        maps[y][x] = str(cnt)
        for i in range(len(dx)):
            search(x+dx[i],y+dy[i], cnt)
        return 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            cnt += search(j, i, cnt)
    print(cnt)