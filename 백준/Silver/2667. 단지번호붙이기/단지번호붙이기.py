import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, li, tmp):
    if x < 0 or x >= n or y < 0 or y>= n or li[x][y] == 0: return
    
    li[x][y] = 0
    tmp.append(1)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        dfs(x+dx[i], y+dy[i], li, tmp)


n = int(input())
li = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0
tmp = []
res = []
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            dfs(i, j, li, tmp)
            res.append(len(tmp))
            cnt += 1
            tmp = []
print(cnt)
res.sort()
print(*res, sep='\n')