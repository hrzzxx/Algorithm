import sys
input = sys.stdin.readline

def solution(a):
    n, m = a
    pw = {}
    for _ in range(n):
        a, b = input().strip().split()
        pw[a] = b
    for _ in range(m):
        print(pw[input().strip()])

solution(map(int, input().split()))