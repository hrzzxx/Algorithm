import sys
input = sys.stdin.readline

x = int(input())
tmp = 10
while True:
    if x > tmp:
        if x%tmp >= 0.5*tmp:
            x = x-(x%tmp) + tmp
        else:
            x -= x%tmp
    else: break
    tmp *= 10
print(x)