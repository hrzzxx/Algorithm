import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().rstrip().split()
    a, b = sorted(list(a)), sorted(list(b))
    if a == b: print('Possible')
    else: print('Impossible')