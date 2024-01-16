import sys
from collections import deque

input = sys.stdin.readline

def solution(tmp):
    n, k = tmp
    queue = deque([i+1 for i in range(n)])
    res = []
    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())
        res.append(queue.popleft())
    return f'<{str(res)[1:-1]}>'
print(solution(map(int, input().split())))