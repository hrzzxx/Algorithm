import sys
input = sys.stdin.readline

n = int(input())
cnt, res = 0, 666

while True:
    if '666' in str(res): cnt += 1
    if cnt == n: break
    res += 1
print(res)