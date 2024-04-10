def solution(s):
    answer = 0
    a,b = 0,0
    x = s[0]
    for i in s:
        if not x: x = i
        
        if i == x: a += 1
        else: b += 1
        
        if a == b:
            answer += 1
            a,b = 0,0
            x = ''
    if a != b: answer += 1
    return answer