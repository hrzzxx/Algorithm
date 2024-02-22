import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []
res = 0
for i in range(n):
    for x in list(map(int, input().split())):
        heapq.heappush(h, x)
        if len(h) > n: heapq.heappop(h)

print(heapq.heappop(h))