import sys
input = sys.stdin.readline

def solution(s):
    zero, one = 0, 0
    for i in s.split('0'): 
        if i: zero += 1
    for i in s.split('1'): 
        if i: one += 1
    print(min(zero, one))

solution(input().strip())