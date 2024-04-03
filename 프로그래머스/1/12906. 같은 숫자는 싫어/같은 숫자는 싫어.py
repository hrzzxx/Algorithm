def solution(arr):
    answer = []
    cur = '*'
    for i in arr:
        if cur == '*': 
            cur = i
            answer.append(cur)
        if i != cur:
            cur = i
            answer.append(cur)
    return answer