import sys
from collections import deque
input = sys.stdin.readline

def solution(n):
    dq = deque([])
    for _ in range(n):
        ex = input().rstrip().split()
        if len(ex) == 1:
            ex = ex[0]
            if ex == 5: print(len(dq))
            else:
                if not dq:
                    if ex == 'empty': print(1)
                    elif ex == 'size': print(0)
                    else: print(-1)
                else:
                    if ex == 'pop_front':print(dq.popleft())
                    elif ex == 'pop_back':print(dq.pop())
                    elif ex == 'front': print(dq[0])
                    elif ex == 'size': print(len(dq))
                    elif ex == 'empty': print(0)
                    else: print(dq[-1])
        else:
            ex, x = ex[0], int(ex[1])
            if ex == 'push_back': dq.append(x)
            else: dq.appendleft(x)
solution(int(input()))