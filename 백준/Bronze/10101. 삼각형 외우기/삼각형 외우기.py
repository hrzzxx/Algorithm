import sys
input = sys.stdin.readline

li = [int(input()) for _ in range(3)]
if sum(li) == 180:
    if len(set(li)) == 1: print('Equilateral')
    elif len(set(li)) == 2: print('Isosceles')
    else: print('Scalene')
else: print('Error')