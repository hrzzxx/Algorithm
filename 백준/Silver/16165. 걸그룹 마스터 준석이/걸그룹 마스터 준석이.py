import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    gname = input().rstrip()
    d[gname] = []
    for _ in range(int(input())):
        pname = input().rstrip()
        d[gname].append(pname)
        d[pname] = gname


for _ in range(m):
    name = input().rstrip()
    quiz = int(input())
    if quiz: print(d[name])
    else:
        res = d[name]
        res.sort()
        print(*res, sep='\n')