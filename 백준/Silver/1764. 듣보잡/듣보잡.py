import sys
input = sys.stdin.readline

def solution(a):
    n, m = a
    a = {input().strip() for _ in range(n)} # 듣도못한
    b = {input().strip() for _ in range(m)} # 보도못한
    res = list(a&b)
    res.sort()
    print(len(res))
    return res

print(*solution(map(int, input().split())), sep='\n')