import sys
input = sys.stdin.readline

for _ in range(int(input())):
    d = dict()
    n = int(input())
    li = list(map(int, input().split()))
    for i in li:
        d[i] = 1
    n2 = int(input())
    li2 = list(map(int, input().split()))
    for i in li2:
        if i in d: print(d[i])
        else: print(0)