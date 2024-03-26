def convert(w):
    if w[0].isalpha():
        return w[0].upper()+w[1:]
    else:
        return w
def solution(s):
    s = s.lower()
    res = ''
    i = 0
    tmp = 1
    while i != len(s):
        if s[i] == ' ':
            res += ' '
            tmp = 1
        else:
            if tmp:
                res += s[i].upper()
                tmp = 0
            else:
                res += s[i]
        i += 1
    return res