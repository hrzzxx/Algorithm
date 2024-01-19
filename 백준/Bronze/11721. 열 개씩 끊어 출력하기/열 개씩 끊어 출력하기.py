import sys
input = sys.stdin.readline

s = input().rstrip()
while len(s) > 10:
    print(s[:10])
    s = s[10:]
print(s)