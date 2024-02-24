import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

li = list('a i u e o'.split())
cnt = 0
for i in s:
    if i in li: cnt += 1
print(cnt)
