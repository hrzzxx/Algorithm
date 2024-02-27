import sys
input = sys.stdin.readline

res = []
for i in range(5):
    res.append((sum(list(map(int, input().split()))), i+1))

tmp = max(res)
print(tmp[1], tmp[0])