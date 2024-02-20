import sys
input = sys.stdin.readline

n, s, p = map(int, input().split())
if n: li = list(map(int, input().split()))
else: li = []

ranking = []
tmp = 0
for i, sc1 in enumerate(li):
    rank = 1
    for j, sc2 in enumerate(li):
        if i==j: continue
        if sc1 < sc2: rank += 1
        if rank > p: 
            rank = -1
            break
    if rank != -1: ranking.append(sc1)
ranking.append(s)
tmp = 0
ranking.sort(reverse=True)
for i, sc1 in enumerate([s]):
    rank = 1
    for j, sc2 in enumerate(ranking):
        if sc1 < sc2:
            rank += 1
            tmp += 1
        elif sc1 == sc2: tmp += 1
        else: break
if tmp > p: print(-1)
else:print(rank)