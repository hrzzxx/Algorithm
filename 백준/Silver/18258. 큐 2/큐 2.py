import sys
from collections import deque
input = sys.stdin.readline

def solution(n):
    queue = deque([])
    for _ in range(n):
        ex = input().split()
        if len(ex) == 1:
            ex = ex[0]
            if ex == 'pop':
                if queue:
                    print(queue.popleft())
                else: 
                    print(-1)
            elif ex == 'size': print(len(queue))
            elif ex == 'empty':
                if queue: print(0)
                else: print(1)
            elif ex == 'front':
                if queue: print(queue[0])
                else: print(-1)
            else:
                if queue: print(queue[-1])
                else: print(-1)
        else: queue.append(int(ex[1]))
solution(int(input()))