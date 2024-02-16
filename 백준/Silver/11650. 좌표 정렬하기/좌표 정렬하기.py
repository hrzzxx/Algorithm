import sys
input = sys.stdin.readline

n = int(input())
li = [tuple(map(int, input().split())) for _ in range(n)]
li.sort(key=lambda x: (x[0], x[1]))
for a,b in li:
    print(a,b)