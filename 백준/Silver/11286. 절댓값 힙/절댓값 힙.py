import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if not x:
        if h: print(heapq.heappop(h)[1])
        else: print(0)
    else:
        heapq.heappush(h, (abs(x), x))