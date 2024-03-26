def solution(k, m, score):
    answer = 0
    score.sort()
    for _ in range(len(score)//m):
        for _ in range(m-1): score.pop()
        p = score.pop()
        answer += p*m
    return answer