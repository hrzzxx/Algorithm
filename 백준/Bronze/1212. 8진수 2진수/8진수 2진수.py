import sys
input = sys.stdin.readline

n = input().rstrip()
print(bin(int(n, 8))[2:])