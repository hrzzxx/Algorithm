import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
q = deque([i+1 for i in range(n)])
res = ''
while q:
    tmp = deque([])
    for _ in range(k-1):
        q.append(q.popleft())
    res += str(q.popleft())+', '

print(f'<{res[:-2]}>')