import sys
input = sys.stdin.readline
for i in range(int(input())): # tc
    dic = {}
    for i in range(int(input())):
        _, t = input().rstrip().split()
        if t in dic.keys(): dic[t] += 1
        else: dic[t] = 1

    tmp = list(dic.values())
    res = 1
    for i in tmp:
        res *= i+1
    print(res-1)