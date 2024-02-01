import sys
input = sys.stdin.readline

li = [int(input()) for _ in range(5)]
a, b, c, d = li[1], li[2], li[3], li[4]
x = a//c
y = b//d
if a%c != 0: x += 1
if b%d != 0: y += 1
print(li[0] - max(x, y))