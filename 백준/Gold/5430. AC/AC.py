import sys
input = sys.stdin.readline

from collections import deque
for i in range(int(input())):
    p = list(input().rstrip())
    n = int(input())
    li = input().rstrip()[1:-1]
    if not li: li = []
    else: li = deque(list(map(int,li.split(','))))
    r = 0
    error = 0
    for i in p:
        if i == 'R': 
            if r: r = 0
            else: r = 1
        else:
            if not li:
                error = 1
                break
            if r: li.pop()
            else: li.popleft()
    if not error: 
        if not li: print("[]")
        else:
            li = list(li)
            if r: li = li[::-1]
            print('[',end='')
            print(*li,sep=',',end='')
            print(']')
    else:
        print('error')