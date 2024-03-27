from collections import Counter
def solution(k, tangerine):
    answer = 0
    tangerine = sorted(dict(Counter(tangerine)).values(), reverse=True)
    tmp = 0
    for i in tangerine:
        tmp += i
        answer += 1
        if tmp >= k: break
    return answer