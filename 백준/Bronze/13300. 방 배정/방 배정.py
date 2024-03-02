import sys
input = sys.stdin.readline

n, k = map(int, input().split())
g, b = [0]*6, [0]*6
for _ in range(n):
    s, y = map(int, input().split())
    if not s: g[y-1] += 1
    else: b[y-1] += 1
res = 0
for i in range(6):
    res += g[i]//k + b[i]//k
    if g[i]%k: res += 1
    if b[i]%k: res += 1
print(res)