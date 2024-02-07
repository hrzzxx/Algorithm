import sys
input = sys.stdin.readline

s = input().rstrip()
p,k,h,t = set(), set(), set(), set()
res = 0
while s:
    tmp, s = s[:3], s[3:]
    if tmp[0] == 'P' and tmp not in p: p.add(tmp)
    elif tmp[0] == 'K' and tmp not in k: k.add(tmp)
    elif tmp[0] == 'H' and tmp not in h: h.add(tmp)
    elif tmp[0] == 'T' and tmp not in t: t.add(tmp)
    else:
        res = 1
        break
if res: print('GRESKA')
else: print(*[13-len(p), 13-len(k), 13-len(h), 13-len(t)])