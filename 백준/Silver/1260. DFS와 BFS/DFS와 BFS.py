import sys
input = sys.stdin.readline

def dfs(nodes, v, li=[]):
    if v not in li: li.append(v)
    nodes[v].sort()
    for i in nodes[v]:
        if i not in li:
            li.append(i)
            dfs(nodes, i, li)
    return li
def bfs(nodes, v, n):
    q = [v]
    res = []
    while q:
        v = q.pop(0)
        res.append(v)
        nodes[v].sort()
        for i in nodes[v]:
            if i not in q and i not in res: q.append(i)
    return res
        

n, m, v = map(int, input().split())
nodes = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
li = []
print(*dfs(nodes, v, li))
print(*bfs(nodes, v, n))