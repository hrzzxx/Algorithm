import sys
from collections import deque
input = sys.stdin.readline

def solution(n):
    queue = deque([])
    for i in range(n):
        queue.append(i+1)
    while True:
        if len(queue) == 1: break
        queue.popleft()
        queue.append(queue.popleft())
    print(queue[0])
solution(int(input()))