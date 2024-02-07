import sys
input = sys.stdin.readline

n = int(input())
res = 0
s = set()
for _ in range(n):
    ip = input().rstrip()
    if ip == 'ENTER': 
        if s: res += len(s)
        s = set()
    else: s.add(ip)
res += len(s)
print(res)