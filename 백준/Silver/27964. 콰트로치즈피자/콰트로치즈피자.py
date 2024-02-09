import sys
input = sys.stdin.readline

n = int(input())
li = input().rstrip().split()
res = set()
c = 'Cheese'
for i in li:
    tmp = i.find(c, len(i)-6)
    if tmp >= 0:
        res.add(i)
if len(res) >= 4: print('yummy')
else: print('sad')
