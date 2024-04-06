import sys
input = sys.stdin.readline

x, y = map(int, input().split())
d = y
m = [31,28,31,30,31,30,31,31,30,31,30,31]
res = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(x-1):
    d += m[i]
print(res[d%7])