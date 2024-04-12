def solution(new_id):
    answer = ''
    for i in new_id:
        if i.isalpha(): i = i.lower()
        elif i.isdigit(): pass
        else:
            if i not in ['-', '_', '.']: i = ''
            else:
                if i == '.' and answer[-1:] == '.': i = ''
        answer += i
    while True:
        if answer and answer[0] == '.': answer = answer[1:]
        if answer and answer[-1] == '.': answer = answer[:-1]
        elif len(answer) >= 16: answer = answer[:15]
        elif not answer: answer = 'a'
        elif len(answer) <= 2:
            tmp = answer[-1]
            while len(answer) != 3:
                answer += tmp
        else: break
        # print(answer)
    return answer