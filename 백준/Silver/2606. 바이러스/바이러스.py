import sys
input = sys.stdin.readline

# 스택
def dfs(nodes, v):
    st = [v]
    res = []
    while st:
        v = st.pop()
        res.append(v)
        for i in nodes[v]:
            if i not in st and i not in res: st.append(i)
    return res

n = int(input())
m = int(input())
nodes = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
li = []
v= 1
print(len(dfs(nodes, v))-1)