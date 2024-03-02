import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

y = 0
m = 0
for i in li:
    y += (i//30+1) * 10
    m += (i//60+1) * 15
if y == m:
    print('Y M',y)
elif y < m:
    print('Y',y)
else: print('M',m)