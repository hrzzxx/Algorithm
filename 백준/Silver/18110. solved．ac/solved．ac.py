import sys
input = sys.stdin.readline

n= int(input())

def round_(x):
    if x%1 >= 0.5:
        return int(x)+1
    else: return int(x)

if n != 0:
    li = [int(input()) for _ in range(n)]
    li.sort()
    p = round_(n*0.15)
    if p>0:
        li = li[p:-p]
        print(round_(sum(li)/(n-(p*2))))
    else: print(round_(sum(li)/n))
else: print(0)
