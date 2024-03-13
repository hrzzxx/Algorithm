import sys
input = sys.stdin.readline

n = int(input())
li = [tuple(input().rstrip().split()) for _ in range(n)]
li.sort(key=lambda x:x[1])
print(li[0][0])