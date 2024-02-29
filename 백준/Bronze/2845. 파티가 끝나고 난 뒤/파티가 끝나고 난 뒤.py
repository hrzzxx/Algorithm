import sys
input = sys.stdin.readline

l, p = map(int, input().split())
li = list(map(int, input().split()))

anw = l*p
for x in li:
    print(x-anw, end=' ')