import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    s,e = map(int, input().split())
    li.append((s,e))
li.sort(key=lambda x:(-x[1],-x[0]))
res = 0
end = -1

while li:
    s,e = li.pop()
    if s >= end:
        res += 1
        end = e
        # print('endtime;', end, 'time;',s,e)
print(res)