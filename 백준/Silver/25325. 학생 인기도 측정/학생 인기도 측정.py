import sys
input = sys.stdin.readline

n = int(input())
li = input().rstrip().split()
d = {name:0 for name in li}
for _ in range(n):
    like = input().rstrip().split()
    for name in like: d[name] += 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for name, sc in d:
    print(name, sc)