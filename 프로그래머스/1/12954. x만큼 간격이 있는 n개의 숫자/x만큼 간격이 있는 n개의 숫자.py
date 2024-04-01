def solution(x, n):
    answer = []
    tmp = 0
    for _ in range(n):
        tmp += x
        answer.append(tmp)
    return answer