def solution(rank, attendance):
    answer = 0
    tmp = []
    for i,r in enumerate(rank):
        if attendance[i]:
            tmp.append((r,i))
    tmp.sort()
    res = [10000,100,1]
    for i in range(3):
        answer += tmp[i][1]*res[i]
    return answer