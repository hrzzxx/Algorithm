import sys
input = sys.stdin.readline

def solution(n):
    snums = [input().strip() for _ in range(n)]
    snums = sorted(snums, key= lambda x: len(x))
    tmp = len(snums[0])
    dic = {}
    def printsnum(dic):
        dic = sorted(dic.items())
        for _, snumlist in dic:
            if len(snumlist) == 1: print(snumlist[0])
            else:
                snumlist.sort()
                print(*snumlist, sep='\n')
    for i in range(n):
        if len(snums[i]) > tmp: 
            tmp=len(snums[i])
            printsnum(dic)
            dic = {}
        sumdigit = 0
        for j in snums[i]:
            if j.isdigit(): sumdigit += int(j)
        if sumdigit in dic.keys():
            dic[sumdigit].append(snums[i])
        else: dic[sumdigit] = [snums[i]]
    printsnum(dic)

solution(int(input()))