import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
li = [w-x, h-y, x-0, y-0]
print(min(li))