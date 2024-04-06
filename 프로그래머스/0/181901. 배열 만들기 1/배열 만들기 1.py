def solution(n, k):
    answer = []
    tmp = 1
    for i in range(k,n+1,k):
        answer.append(i)
        
    return answer