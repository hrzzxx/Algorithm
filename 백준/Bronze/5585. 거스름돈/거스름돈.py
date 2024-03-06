import sys
input = sys.stdin.readline

n = 1000- int(input())

coins = [500,100,50,10,5,1]
tmp = 0
res = 0
while n:
    if n >= coins[tmp]:
        n-= coins[tmp]
        res += 1
    else: tmp += 1
print(res)