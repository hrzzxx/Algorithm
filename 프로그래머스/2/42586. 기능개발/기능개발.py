def solution(progresses, speeds):
    answer = []
    cur = 0
    cnt = 0
    for i in range(len(progresses)):
        tmp = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]:
            tmp += 1
        # print(tmp)
        if not cur: 
            cur = tmp
            cnt += 1
        else:
            if cur >= tmp:
                cnt += 1
            else:
                cur = tmp
                answer.append(cnt)
                cnt = 1
    answer.append(cnt)
    return answer