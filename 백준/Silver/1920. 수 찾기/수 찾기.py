import sys
input = sys.stdin.readline

n = int(input())
a1 = set(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

for j in a2:
    if a1&{j}: print(1)
    else: print(0)