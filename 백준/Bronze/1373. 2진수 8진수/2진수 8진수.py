import sys
input = sys.stdin.readline

n = input().rstrip()
print(oct(int(n, 2))[2:])