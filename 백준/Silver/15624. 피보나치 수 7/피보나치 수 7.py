import sys
input = sys.stdin.readline

n = int(input()) # max_input: 10**18
if n == 0:
    print(0)
else:
    a,b = 0,1
    n %= 1000000007
    for i in range(2,n+1):
        a,b = b%(1000000007),(a+b)%(1000000007)
    print(b)