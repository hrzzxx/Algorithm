import sys
input = sys.stdin.readline
import math

n = str(math.factorial(int(input())))[::-1]
cnt = 0
for i in n:
    if i != '0':
        print(cnt)
        break
    cnt += 1