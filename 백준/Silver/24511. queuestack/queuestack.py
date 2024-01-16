import sys
from collections import deque

input = sys.stdin.readline

def solution(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))

    dq = deque([])
    for i, ds in enumerate(a):
        if not ds:
            dq.appendleft(b[i])
    if not dq:
        print(*c)
    else:
        for i in c:
            dq.append(i)
            print(dq.popleft(), end=' ')

solution(int(input()))