import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))
res =[]
for i in test:
    if i in cards: res.append(1)
    else: res.append(0)
print(*res)