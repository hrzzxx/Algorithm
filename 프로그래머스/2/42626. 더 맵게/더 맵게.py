import heapq
def solution(scoville, K):
    answer = 0
    h = scoville
    heapq.heapify(h)
    
    tmp = -1
    for _ in range(len(scoville)-1):
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        if a >= K:
            return answer

        heapq.heappush(h, a+b*2)
        answer+=1
        
    if heapq.heappop(h) > K: return answer
    else: return -1
        