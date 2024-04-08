def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ': 
            answer += ' '
            continue
        ord_ = ord(i) + n
        if i.islower():
            if ord_ > 122:
                ord_ -= 26
        else:
            if ord_ > 90: ord_ -= 26
        answer += chr(ord_)
    return answer