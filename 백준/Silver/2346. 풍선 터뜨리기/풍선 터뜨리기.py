import sys
from collections import deque

input = sys.stdin.readline

def solution(n):
    dq = deque([i+1 for i in range(n)])
    li = list(map(int, input().split()))
    dic = {}
    for i in range(n): dic[i+1] = li[i]
    k = dq.popleft()
    res = [k]
    while dq:
        if dic[k] >=0:
            for i in range(dic[k]-1):
                dq.append(dq.popleft())
            k = dq.popleft()
        else:
            for _ in range((-dic[k])-1):
                dq.appendleft(dq.pop())
            k = dq.pop()
        res.append(k)
    return res
        
        
print(*solution(int(input())))