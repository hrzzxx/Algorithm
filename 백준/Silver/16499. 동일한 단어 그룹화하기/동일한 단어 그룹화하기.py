import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    w = list(input().rstrip())
    w.sort()
    s.add(''.join(w))
print(len(s))