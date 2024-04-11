from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque([])
    for i in cities:
        i = i.lower()
        if i in q:
            q.remove(i)
            q.append(i)
            answer += 1
        else:
            answer += 5
            if cacheSize == 0: continue
            if len(q) < cacheSize:
                q.append(i)
            else:
                q.popleft()
                q.append(i)
                
    return answer