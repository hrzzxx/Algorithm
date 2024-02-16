import sys
input = sys.stdin.readline

eng_ = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'.split(', ')
eng = {eng_[i]: i+1 for i in range(len(eng_))}

r = 31
M = 1234567891
l = int(input())
s = input().rstrip()
res = 0
for i in range(l):
    res += eng[s[i]] * (r**i)

print(res%M)
