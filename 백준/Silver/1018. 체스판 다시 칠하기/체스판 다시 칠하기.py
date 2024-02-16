import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [list(input().rstrip()) for _ in range(n)]
b = [[] for _ in range(n)]
w = [[] for _ in range(n)]


for i in range(n):
    for j in range(m):
        c = chess[i][j]
        if i%2 == 0: # 홀수 라인
            if j%2 == 0: # 홀수 말
                if c == 'B': 
                    b[i].append(0)
                    w[i].append(1)
                else: 
                    b[i].append(1)
                    w[i].append(0)
                    chess[i][j] = 'B'
            else: # 짝수 말
                if c == 'B': 
                    b[i].append(1)
                    w[i].append(0)
                    chess[i][j] = 'W'
                else: 
                    b[i].append(0)
                    w[i].append(1)
        else: # 짝수 라인
            if j%2 == 0:
                if c == 'W': 
                    b[i].append(0)
                    w[i].append(1)
                else: 
                    b[i].append(1)
                    w[i].append(0)
            else:
                if c == 'W': 
                    b[i].append(1)
                    w[i].append(0)
                else: 
                    b[i].append(0)
                    w[i].append(1)


res = 9999999
for i in range(n-7):
    b_ = b[i:8+i]
    w_ = w[i:8+i]
    for j in range(m-7):
        bb, ww = 0,0
        for k in range(8):
            bb += sum(b_[k][j:8+j])
            ww += sum(w_[k][j:8+j])
        tmp = min(bb, ww)
        res = min(res, tmp)
print(res)
