import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    res = (a%10+10)**(b%4+4)%10
    if not res: print(10)
    else: print(res)