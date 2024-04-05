import heapq
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x:-x[0])
    h = []
    l = len(jobs)
    time = 0
    while True:
        if not jobs and not h: break
        
        while jobs:
            req, lead = jobs.pop()
            if req <= time:
                heapq.heappush(h,[lead, req])
            else:
                jobs.append([req,lead])
                break
        if h:
            lead_time, req_time = heapq.heappop(h)
            answer += (time-req_time)+lead_time
            time += lead_time
        else:
            time += 1
            
    return answer//l