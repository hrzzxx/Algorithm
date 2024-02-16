import sys
input = sys.stdin.readline

def solution():
    
    if a**2+b**2 == c**2:
        return 'right'
    else: return 'wrong'

while True:
    li = list(map(int, input().split()))
    li.sort()
    a, b, c = li[0], li[1], li[2]
    if (a,b,c) == (0,0,0): break
    
    print(solution())