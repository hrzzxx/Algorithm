import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []
for i in range(1,n+1):
    if not n%i: li.append(i)
try:
    print(li[k-1])
except:
    print(0)