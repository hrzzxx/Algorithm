import sys
input = sys.stdin.readline

n = int(input())
def solution():
    cur = 1
    while cur < n:
        tmp = cur
        for i in str(cur):
            tmp += int(i)
        if tmp == n: 
            return cur
        cur += 1
    return 0
print(solution())