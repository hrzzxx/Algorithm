import sys
input = sys.stdin.readline

n = int(input())
d = dict()
for _ in range(n):
    name = input().rstrip()
    if name in d: d[name] += 1
    else: d[name] = 1
for _ in range(n-1):
    name = input().rstrip()
    d[name] -= 1
d = sorted(d.items(), key=lambda x:-x[1])
print(d[0][0])