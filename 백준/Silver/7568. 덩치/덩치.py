import sys
input = sys.stdin.readline

li = [tuple(map(int, input().split())) for _ in range(int(input()))]

for i, (x, y) in enumerate(li):
    rank = 1
    for j, (p, q) in enumerate(li):
        if i==j: continue
        if x<p and y <q: rank += 1
    print(rank, end=' ')
