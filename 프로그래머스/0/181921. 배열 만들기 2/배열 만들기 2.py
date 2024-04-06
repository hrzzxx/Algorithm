def solution(l, r):
    answer = []
    tmp = {'5','0'}
    for i in range(l,r+1):
        _i = set(list(str(i)))
        # print(_i)
        if not _i-tmp:
            answer.append(i)
    if not answer: answer = [-1]
    return answer