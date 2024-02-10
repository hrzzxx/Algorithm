import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
cnt = 0
i = 0
while True:
    if i == k: break
    if li[i] == -1:
        cnt = -1
        break
    tmp = i
    i = li[i]
    li[tmp] = -1
    cnt += 1
print(cnt)