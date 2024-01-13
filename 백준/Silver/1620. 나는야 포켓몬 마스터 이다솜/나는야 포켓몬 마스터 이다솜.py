import sys
input = sys.stdin.readline

def solution(a):
    n, m = a
    monsters = {}
    monsters2 = {}
    for i in range(n):
        tmp = input().strip()
        monsters[i+1] = tmp
        monsters2[tmp] = i+1
    for _ in range(m):
        tmp = input().strip()
        if tmp.isdigit(): print(monsters[int(tmp)])
        else: print(monsters2[tmp])

solution(map(int, input().split()))