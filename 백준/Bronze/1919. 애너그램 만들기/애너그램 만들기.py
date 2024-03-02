import sys
input = sys.stdin.readline
import string

alpha = string.ascii_lowercase
d1 = {i:0 for i in alpha}
d2 = {i:0 for i in alpha}

a = input().rstrip()
b = input().rstrip()
for i in a:
    d1[i] += 1
res = 0
for i in b:
    d2[i] += 1
d1, d2 = list(d1.values()), list(d2.values())
for i in range(len(d1)):
    res += abs(d1[i]-d2[i])
print(res)

