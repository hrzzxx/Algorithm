import sys
input = sys.stdin.readline

d = dict()
for _ in range(int(input())):
    book = input().rstrip()
    if book in d: d[book] += 1
    else: d[book] = 1

d = sorted(d.items(), key=lambda x:(-x[1], x[0]))
print(d[0][0])