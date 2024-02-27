import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    h_min = []
    h_max = []
    k = int(input())
    visited = [False] * k
    for i in range(k):
        cmd, num = input().rstrip().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(h_min, (num, i))
            heapq.heappush(h_max, (-num, i))
        else:
            if not h_min: continue
            if num == 1:
                while h_max and visited[h_max[0][1]]:
                    heapq.heappop(h_max)
                if h_max: visited[heapq.heappop(h_max)[1]] = True
            else:
                while h_min and visited[h_min[0][1]]:
                    heapq.heappop(h_min)
                if h_min: visited[heapq.heappop(h_min)[1]] = True

    while h_max and visited[h_max[0][1]]: heapq.heappop(h_max)
    while h_min and visited[h_min[0][1]]: heapq.heappop(h_min)
    
    if not h_min: print('EMPTY')
    else:
        print(-heapq.heappop(h_max)[0], heapq.heappop(h_min)[0])