import sys
input = sys.stdin.readline

def solution(s):
    step = len(s)-1
    for i in range(len(s)):
        tmp = set()
        for j in range(step):
            tmp.add(s[j]+s[j+i+1])
        if len(tmp) != step: return f'{s} is NOT surprising.'
        step -=1

    return f'{s} is surprising.'

while True:
    s = input().strip()
    if s == '*': break
    print(solution(s))