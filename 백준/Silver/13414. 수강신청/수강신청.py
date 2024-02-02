import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dic = dict()
for i in range(k):
    idnum = input().rstrip()
    dic[idnum] = i

dic = sorted(dic.items(), key=lambda x:x[1])
for i in dic[:n]: print(i[0])