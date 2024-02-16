import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()
# print(li)
print(round(sum(li)/n))
print(li[n//2])
tmp = Counter(li).most_common(2)
if len(tmp) == 1: print(tmp[0][0])
elif tmp[0][1] > tmp[1][1]: print(tmp[0][0])
else: print(tmp[1][0])
print(li[-1]-li[0])