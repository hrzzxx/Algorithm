def solution(X, Y):
    answer = ''
    li = []
    s = set(X)&set(Y)
    if not s: return "-1"
    if s == {"0"}: return "0"
    s = list(s)
    s.sort(reverse=True)
    for i in s:
        answer += i*min(X.count(i), Y.count(i))
    return answer