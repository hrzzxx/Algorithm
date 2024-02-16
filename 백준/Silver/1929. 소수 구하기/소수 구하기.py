import sys
input = sys.stdin.readline

m, n = map(int, input().split())

nums = set(range(2, n+1))
prime = set()
for i in range(2, n+1):
    if i in nums:
        if i >= m: print(i)
        nums -= set(range(i, n+1, i))