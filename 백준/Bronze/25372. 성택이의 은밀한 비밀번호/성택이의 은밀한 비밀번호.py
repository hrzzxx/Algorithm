import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = input().rstrip()
    if 6<=len(n)<=9: print('yes')
    else:print('no')