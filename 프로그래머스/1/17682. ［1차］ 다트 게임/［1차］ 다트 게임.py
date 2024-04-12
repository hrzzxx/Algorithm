def solution(dartResult):
    answer = 0
    res = []
    sc = ''
    sdt = {'S':1, 'D':2, 'T':3}
    award = ['*','#']
    for i in dartResult:
        if i.isdigit(): sc += i
        elif i in sdt:
            sc = int(sc)
            res.append(sc**sdt[i])
            sc = ''
        else:
            if i == '*':
                res[-1] *= 2
                if len(res) > 1:
                    res[-2] *= 2
            else:
                res[-1] = -res[-1]
    return sum(res)