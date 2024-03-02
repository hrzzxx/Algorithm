import sys
input = sys.stdin.readline
import itertools

li = [int(input()) for _ in range(9)]
li = list(itertools.combinations(li, 7))

for i in li:
    i = list(i)
    if sum(i) == 100:
        i.sort()
        print(*i, sep='\n')
        break