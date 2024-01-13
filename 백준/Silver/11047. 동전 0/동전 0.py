import sys
input = sys.stdin.readline

def solution(a):
    n, m = a
    coins = [int(input()) for _ in range(n)]
    res = 0
    for i in coins[::-1]:
        if m == 0: break
        if m%i != m:
            res += m//i
            m %= i
    print(res)

solution(map(int, input().split()))