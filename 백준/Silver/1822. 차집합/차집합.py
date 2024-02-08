import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

res = list(a-b)
print(len(res))
if res:
    res.sort()
    print(*res)