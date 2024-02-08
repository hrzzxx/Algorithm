import sys
input = sys.stdin.readline

d = dict()
cnt = 0
while True:
    s = input().rstrip()
    if s == '': break
    if s in d: d[s] += 1
    else: d[s] = 1
    cnt += 1

d = sorted(d.items())
for name, n in d:
    print(name, "%.4f" %(n/cnt*100))