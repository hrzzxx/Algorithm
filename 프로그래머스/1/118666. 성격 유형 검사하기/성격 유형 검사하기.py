def solution(survey, choices):
    answer = ''
    test = "RTCFJMAN"
    d = {x:0 for x in test}
    for s, c in zip(survey, choices):
        if c == 4: continue
        elif c < 4:
            d[s[0]] += 4-c
        else:
            d[s[1]] += c-4
    for i in range(0,8,2):
        a, b = d[test[i]], d[test[i+1]]
        if a >= b: answer += test[i]
        else: answer += test[i+1]
    return answer