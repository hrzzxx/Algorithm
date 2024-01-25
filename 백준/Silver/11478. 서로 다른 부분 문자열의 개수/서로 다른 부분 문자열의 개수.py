import sys
input = sys.stdin.readline

s = input().rstrip()
res = set(list(s))
for i in range(len(s)):
    for j in range(i):
        res.add(s[j:len(s)-i+1+j])
print(len(res))