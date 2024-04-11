from collections import Counter
def solution(N, stages):
    answer = []
    counter = Counter(stages)
    
    len_ = len(stages)
    li = []
    for i in range(1,N+1):
        cnt = counter[i]
        if not cnt: li.append((0,i))
        else:
            li.append((cnt/len_, i))
            len_ -= cnt
    li.sort(key=lambda x:(-x[0],x[1]))
    for _, i in li:
        answer.append(i)
    return answer