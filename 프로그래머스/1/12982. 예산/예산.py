def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while budget and d:
        cur = d.pop()
        if budget < cur: break
        else:
            budget -= cur
            answer += 1
    return answer