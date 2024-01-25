import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    name, state = input().rstrip().split()
    if state == 'enter': s.add(name)
    else: s.remove(name)

print(*sorted(list(s), reverse=True), sep='\n')