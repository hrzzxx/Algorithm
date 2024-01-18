import sys
from collections import deque

input = sys.stdin.readline

def solution(nm):
    n, m = nm
    docs = deque([(i, x) for i, x in enumerate(list(map(int, input().split())))])
    step = 0
    imp = max(docs, key=lambda x: x[1])
    while True:
        imp = max(docs, key=lambda x: x[1])[1]
        if docs[0][1] == imp:
            step += 1
            tmp = docs.popleft()
            if tmp[0] == m: return step
        else:
            docs.append(docs.popleft())

for _ in range(int(input())):
    print(solution(map(int, input().split())))
