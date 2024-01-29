import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n<m:
        n, m = m, n
    print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))