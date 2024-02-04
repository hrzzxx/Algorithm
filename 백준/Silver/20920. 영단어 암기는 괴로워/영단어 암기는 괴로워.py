import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
for _ in range(n):
    w = input().rstrip()
    if len(w) >= m:
        if w not in d.keys(): d[w] = 1
        else: d[w] += 1

# lambda 다중 조건 설정
d = sorted(d.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for w,_ in d: print(w)