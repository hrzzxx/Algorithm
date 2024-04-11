def solution(s, skip, index):
    answer = ''
    skip_ = [ord(i) for i in skip]
    skip_.sort()
    for i in s:
        i = ord(i)
        cnt = 0
        while cnt != index:
            i += 1
            if i > 122: i -= 26
            if i not in skip_: cnt += 1
        answer += chr(i)
    return answer