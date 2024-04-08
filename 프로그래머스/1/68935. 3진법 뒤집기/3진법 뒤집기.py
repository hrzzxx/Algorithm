def solution(n):
    answer = 0
    tmp = ''
    while n:
        tmp += str(n%3)
        n//=3
    for i, j in enumerate(tmp[::-1]):
        j = int(j)
        if j: answer += j*(3**i)
    return answer