import sys
input = sys.stdin.readline

def solution(a):
    li=list(map(int, input().split()))
    li.sort()
    res = 0
    for i in range(a):
        res += sum(li[:i+1])
    print(res)

solution(int(input()))