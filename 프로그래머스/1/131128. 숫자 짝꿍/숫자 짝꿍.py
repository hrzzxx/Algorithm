from collections import Counter
def solution(X, Y):
    answer = ''
    s = set(X)&set(Y)
    if not s: return "-1"
    if s == {"0"}: return "0"
    s = list(s)
    s.sort(reverse=True)
    x,y = Counter(X), Counter(Y)
    for i in s:
        answer += i*min(x[i], y[i])
    return answer