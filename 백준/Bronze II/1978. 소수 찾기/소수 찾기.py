import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

mx = li[-1]

s = set(range(2, mx+1))
res = set()
for i in range(2,mx+1):
    if i in s:
        res.add(i)
        s -= set(range(0, mx+1, i))
print(len(set(li)&res))