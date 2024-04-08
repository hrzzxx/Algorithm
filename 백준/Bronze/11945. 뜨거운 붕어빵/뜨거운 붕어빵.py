import sys
input = sys.stdin.readline

x, y = map(int, input().split())
for _ in range(x):
    print(input().rstrip()[::-1])