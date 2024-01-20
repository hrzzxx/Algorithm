import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == 'end': break

    a = 'a e i o u'.split()
    s_ = list(s)
    cnt1,cnt2 = 0,0
    res = 1
    tg =0
    cur = ''
    for i in s_:
        if cur == i and i not in ['e', 'o']: 
            res = 0
            break
        if i in a:
            if not tg: tg = 1
            cnt1 += 1
            if cnt1 == 3:
                res = 0 
                break
            cnt2 = 0
        else:
            cnt2 += 1
            if cnt2 == 3: 
                res = 0
                break
            cnt1 = 0
        cur = i
    if not res or not tg: print(f'<{s}> is not acceptable.')
    else: print(f'<{s}> is acceptable.')