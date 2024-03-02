import sys
input = sys.stdin.readline

for _ in range(3):
    li = list(map(int, input().split()))
    a = li.count(0)
    if a == 1: print('A')
    elif a == 2: print('B')
    elif a == 3: print('C')
    elif a == 4: print('D')
    else: print('E')