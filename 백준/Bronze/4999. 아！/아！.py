import sys
input = sys.stdin.readline

s1 = len(input().rstrip())
s2 = len(input().rstrip())
if s1 >= s2: print('go')
else: print('no')