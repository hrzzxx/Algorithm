import sys
input = sys.stdin.readline

for _ in range(int(input())):
    li = list(map(int, input().split()))
    n, li = li[0], li[1:]
    tmp = n//2
    d = dict()
    for i in li:
        if i in d: d[i] += 1
        else: d[i] = 1
    d = sorted(d.items(), key=lambda x: -x[1])
    if d[0][1] > tmp: print(d[0][0])
    else: print('SYJKGW')