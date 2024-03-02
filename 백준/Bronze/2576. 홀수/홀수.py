import sys
input = sys.stdin.readline

res = 0
min_ = 99999
for _ in range(7):
    x = int(input())
    if x % 2 != 0:
        res += x
        min_ = min(min_, x)
if not res: print(-1)
else: print(res, min_, sep='\n')