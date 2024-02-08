import sys
input = sys.stdin.readline
import itertools

n = int(input())
k = int(input())
li = [input().rstrip() for _ in range(n)]
res = list(itertools.permutations(li, k))
s = set()
for i in res: s.add(''.join(i))
print(len(s))