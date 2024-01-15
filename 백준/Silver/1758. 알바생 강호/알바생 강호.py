import sys
input = sys.stdin.readline

def solution(n):
    res = 0
    li = [int(input()) for _ in range(n)]
    li.sort(reverse=True)
    for i in range(n):
        tmp = li[i] - i
        if tmp>0: res += tmp
    return res

print(solution(int(input())))