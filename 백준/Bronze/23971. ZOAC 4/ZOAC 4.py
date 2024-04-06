import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())
a,b = 0,0
for i in range(1,w+1,m+1):
    a += 1
for j in range(1, h+1, n+1):
    b += 1
print(a*b)