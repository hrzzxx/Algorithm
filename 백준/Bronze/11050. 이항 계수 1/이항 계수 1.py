import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
print(math.factorial(n)//(math.factorial(m)*math.factorial(n-m)))