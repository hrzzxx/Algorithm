import sys
input = sys.stdin.readline

n = input().rstrip()
li = [1]*10
res = 1
def tmp(res, li):
    res = res+1
    li = [i+1 for i in li]
    return res, li
for i in n:
    i = int(i)
    if i not in [6, 9] and not li[i]: 
        res , li = tmp(res, li)
        li[i] -= 1
    elif i == 6 and not li[i] and li[9]:
        li[9] -= 1
    elif i == 9 and not li[i] and li[6]:
        li[6] -= 1
    elif i in [6, 9] and not li[i]:
        res, li = tmp(res, li)
        li[i] -= 1
    else:
        li[i] -= 1
    # print(li)
print(res)
