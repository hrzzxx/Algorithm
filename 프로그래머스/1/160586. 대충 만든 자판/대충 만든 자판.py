def solution(keymap, targets):
    answer = []
    d = {}
    for word in targets:
        cnt = 0
        for i in word:
            if i in d:
                pass
            else:
                num = -1
                for keys in keymap:
                    if i in keys:
                        if num != -1: num = min(num,keys.index(i)+1)
                        else: num = keys.index(i)+1
                if num == -1:
                    cnt = -1
                    break
                cnt += num
        answer.append(cnt)
    return answer