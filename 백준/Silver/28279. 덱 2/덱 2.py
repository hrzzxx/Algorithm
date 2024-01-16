import sys
from collections import deque
input = sys.stdin.readline

def solution(n):
    dq = deque([])
    for _ in range(n):
        ex = input().rstrip()
        if len(ex) == 1:
            ex = int(ex[0])
            if ex == 5: print(len(dq))
            else:
                if not dq:
                    if ex == 6: print(1)
                    else: print(-1)
                else:
                    if ex == 3:print(dq.popleft())
                    elif ex == 4:print(dq.pop())
                    elif ex == 6: print(0)
                    elif ex == 7: print(dq[0])
                    else: print(dq[-1])
        else:
            ex, x = map(int, ex.split())
            if ex == 1: dq.appendleft(x)
            else: dq.append(x)
solution(int(input()))