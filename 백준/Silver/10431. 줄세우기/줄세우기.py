import sys
input = sys.stdin.readline
from collections import deque

P = int(input())

for i in range(P):
    li = deque(list(map(int, input().split())))
    t = li[0]
    li.popleft()

    q = deque([])
    min_ = 0
    res = 0
    while li:
        cur = li.popleft()
        if not min_: 
            min_ = cur
            q.append(min_)
        else:
            if cur < min_: min_ = cur
            st = []
            while q:
                tmp = q.pop()
                if tmp < cur:
                    q.append(tmp)
                    break
                else:
                    st.append(tmp)
            q.append(cur)
            res += len(st)
            while st:
                q.append(st.pop())
    print(t, res)