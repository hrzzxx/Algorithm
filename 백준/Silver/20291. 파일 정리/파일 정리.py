import sys
input = sys.stdin.readline

li = [input().rstrip().split('.')[1] for _ in range(int(input()))]
d = dict()
for i in li:
    if i in d: d[i] += 1
    else: d[i] = 1
d = sorted(d.items())
for name, count in d:
    print(name, count)