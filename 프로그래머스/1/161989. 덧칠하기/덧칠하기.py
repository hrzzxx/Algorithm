def solution(n, m, section):
    answer = 0
    li = [0]*(n+1)
    tmp = []
    sec = set(section)
    
    for i in section:
        if i in sec:
            cur = set(range(i,i+m))
            # print(sec, cur, sec&cur)
            if sec & cur: answer += 1
            # answer += len(sec & cur)
            sec -= cur
            if not sec: break
    return answer