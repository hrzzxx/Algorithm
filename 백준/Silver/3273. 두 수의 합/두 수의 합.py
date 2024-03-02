import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
d = {}
for i in li:
    if i in d: d[i] += 1
    else: d[i] = 1
x = int(input())
res = 0
for i in d:
    if x-i != i and x-i in d and d[i]: 
        res += 1
        d[i] -= 1
        d[x-i] -= 1
print(res)