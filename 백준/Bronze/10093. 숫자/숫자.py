import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a > b:
    a, b = b, a

if a == b:
    print(0)
else:
    print(b-a-1)
    print(*range(a+1, b))