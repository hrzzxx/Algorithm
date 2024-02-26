import sys
input = sys.stdin.readline
import heapq

h = []
for _ in range(int(input())):
    li = list(map(int, input().split()))
    a, li = li[0], li[1:]
    if a == 0:
        if h:
            print(heapq.heappop(h)[1])
        else: print(-1)
    else:
        for i in li:
            heapq.heappush(h, (-i, i))