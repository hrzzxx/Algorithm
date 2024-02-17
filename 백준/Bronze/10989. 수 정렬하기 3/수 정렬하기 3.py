import sys
input = sys.stdin.readline

d = {i+1: 0 for i in range(10001)}
for _ in range(int(input())):
    d[int(input())] += 1

for a, b in d.items():
    for _ in range(b):
        sys.stdout.write(str(a)+'\n')
