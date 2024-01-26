import sys
input = sys.stdin.readline

while True:
    li = list(map(int, input().split()))
    if sum(li) == 0: break
    li.sort()
    if li[0]+li[1] > li[2]:
        if len(set(li)) == 1: print('Equilateral')
        elif len(set(li)) == 2: print('Isosceles')
        else: print('Scalene')
    else:
        print('Invalid')