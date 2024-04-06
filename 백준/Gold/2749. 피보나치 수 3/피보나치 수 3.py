import sys
input = sys.stdin.readline

n = int(input()) # max_input: 10**18
if n == 0:
    print(0)
else:
    a,b = 0,1
    # 피사노주기
    # m==10**k (k>2), 주기 = 15*10**(k-1)
    # k = 나눌 수 (10**6)
    n %= 15*(10**5)
    for i in range(2,n+1):
        a,b = b%(10**6),(a+b)%(10**6)
    print(b)