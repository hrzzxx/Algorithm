def solution(t, p):
    l = len(p)
    p = int(p)
    res = 0
    for i in range(len(t)-l+1):
        tmp = int(t[i:l+i])
        if tmp <= p: res += 1
        
    return res