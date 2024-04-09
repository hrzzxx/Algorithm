def solution(name, yearning, photo):
    answer = []
    d = dict()
    for n, y in zip(name, yearning):
        d[n] = y
    for p in photo:
        res = 0
        for i in p:
            if i in d:
                res += d[i]
        answer.append(res)
    return answer