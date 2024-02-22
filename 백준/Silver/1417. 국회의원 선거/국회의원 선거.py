import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []
cur = -int(input())
for i in range(n-1):
    x = int(input())
    heapq.heappush(h, -x)
res = 0
if not h: print(res)
else:
    while True:
        v = heapq.heappop(h)
        if cur < v:
            break     
        cur -= 1
        heapq.heappush(h, v+1)
        res += 1
    print(res)