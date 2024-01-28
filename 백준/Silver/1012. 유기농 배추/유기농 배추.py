import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

tc = int(input())
def dfs(x, y, li):
    if x < 0 or x >= n or y < 0 or y>= m or li[x][y] == 0: return
    
    li[x][y] = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        dfs(x+dx[i], y+dy[i], li)

for _ in range(tc):
    m, n, k = map(int, input().split())
    li = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        li[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                dfs(i, j, li)
                cnt += 1
    print(cnt)

