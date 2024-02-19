import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

li.sort(reverse=True)
print(*li, sep='\n')