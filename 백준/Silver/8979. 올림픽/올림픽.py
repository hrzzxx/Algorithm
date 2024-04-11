import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x:(-x[1], -x[2], -x[3]))
cur = []
rank = 0
tmp = 0
for i in li:
    idx, medal = i[0], i[1:]
    if medal == cur:
        tmp += 1
    else:
        cur = medal
        rank += 1+tmp
        tmp = 0
    
    if idx == k: 
        print(rank)
        break
    