import sys
input = sys.stdin.readline

li = []
for n in range(1,10001):
    if n not in li:
        print(n)
    tmp = n
    n = str(n)
    for i in n:
        tmp += int(i)
    n = tmp
    li.append(n)