import sys
input = sys.stdin.readline

def solution(a):
    s = set()
    for _ in range(a):
        tmp = input().strip().split()
        if len(tmp) > 1:
            c, n = tmp[0], int(tmp[1])
            if c == 'add': s.add(n)
            elif c == 'remove': 
                if n in s: s.remove(n)
            elif c == 'check':
                if n in s: print(1)
                else: print(0)
            elif c == 'toggle':
                if n in s: s.remove(n)
                else: s.add(n)
        else: 
            c = tmp[0]
            if c == 'all': s = {i+1 for i in range(20)}
            elif c == 'empty': s = set()

solution(int(input()))