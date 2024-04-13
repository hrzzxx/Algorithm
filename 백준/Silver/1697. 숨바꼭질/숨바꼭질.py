import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
if n>m: print(n-m)
else:
    maps = [0]*(m+2)
    q = deque([n])
    dx = [-1,1]
    maps[n] = 1
    res = 0
    while q:
        x = q.popleft()
        for i in range(3):
            if i > 0: nx = x+dx[i-1]
            else: nx = x*2
            if 0<=nx<=m+1 and not maps[nx]: 
                q.append(nx)
                maps[nx] = maps[x]+1
                if nx == m: 
                    res = maps[x]
                    break 
    print(res)
