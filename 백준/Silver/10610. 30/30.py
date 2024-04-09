import sys
input = sys.stdin.readline

n = list(map(int,list(input().rstrip())))
# 배수 판정법 (30) : 3의 배수 and 10의 배수
# 배수 판정법 (3) : 각 자릿수의 합이 3의 배수
if 0 not in n: print(-1)
else:
    if sum(n) % 3: # 3의 배수
        print(-1)
    else:
        n.sort(reverse=True)
        print(''.join(list(map(str,n))))