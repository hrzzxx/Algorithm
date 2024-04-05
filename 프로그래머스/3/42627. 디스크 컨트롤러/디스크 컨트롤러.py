import heapq
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x:-x[0])
    h = []
    l = len(jobs)
    time, ex, cur_time = 0,0,1
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
            # ex = 1
            time += lead_time
        else:
            time += 1
        # else:
        #     cur_time += 1
        #     if cur_time == lead_time:
        #         cur_time = 1
        #         ex = 0
        # time += 1
            
    return answer//l