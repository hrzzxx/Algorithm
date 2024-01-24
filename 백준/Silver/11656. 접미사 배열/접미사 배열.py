import sys
input = sys.stdin.readline

res = []
s = input().rstrip()
for i in range(len(s)):
    res.append(s)
    s = s[1:]
res.sort()
print(*res, sep='\n')