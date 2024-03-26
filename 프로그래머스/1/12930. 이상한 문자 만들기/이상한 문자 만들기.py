def convert(s):
    res=''
    for i,w in enumerate(s):
        if i%2: res += w.lower()
        else: res += w.upper()
    return res
def solution(s):
    res = ''
    tmp = ''
    for i in s:
        if i==' ':
            if tmp: 
                res += convert(tmp)
                tmp=''
            res += ' '
        else:
            tmp += i
    if tmp: res += convert(tmp)
    return res