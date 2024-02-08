import sys
input = sys.stdin.readline

n, c = map(int, input().split())
li = list(map(int, input().split()))
d = dict()
for i in li:
    if i in d: d[i] += 1
    else: d[i] = 1
d = sorted(d.items(), key=lambda x: -x[1])
for i in d:
    print(*[i[0]]*i[1], end=' ')