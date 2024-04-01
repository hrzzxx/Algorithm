def solution(n):
    answer = 0
    for i in range(n,0,-1):
        if not n%i: answer += i
    return answer