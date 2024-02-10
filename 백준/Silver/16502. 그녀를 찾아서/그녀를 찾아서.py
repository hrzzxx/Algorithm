import sys
input = sys.stdin.readline

time = int(input())
m = int(input())

# graph = {'A':[0]*4, 'B':[0]*4, 'C':[0]*4, 'D':[0]*4}
graph = [[0]*4, [0]*4, [0]*4, [0]*4]
def fn(b):
    if b == 'A': return 0
    elif b== 'B': return 1
    elif b == 'C': return 2
    else: return 3
for _ in range(m):
    a, b, per = input().rstrip().split()
    per = float(per)
    a, b = fn(a), fn(b)
    graph[b][a] = per
res = [25]*4
for _ in range(time):
    tmp = [0]*4
    for i in range(4):
        tmp[0] += res[i] * graph[0][i]
        tmp[1] += res[i] * graph[1][i]
        tmp[2] += res[i] * graph[2][i]
        tmp[3] += res[i] * graph[3][i]
    res = tmp
for i in res:
    print(f'{i:.2f}')