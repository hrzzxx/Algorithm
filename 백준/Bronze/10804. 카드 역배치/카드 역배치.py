import sys
input = sys.stdin.readline

li = list(range(1,21))
for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    li = li[:a]+li[a:b][::-1]+li[b:]
print(*li)