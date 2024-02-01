import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    a, b = input().rstrip().split()
    a = int(a)
    if a not in dic.keys(): dic[a] = []
    dic[a].append(b)

dic = sorted(dic.items())
for i in dic:
    for j in i[1]:
        print(i[0], j)