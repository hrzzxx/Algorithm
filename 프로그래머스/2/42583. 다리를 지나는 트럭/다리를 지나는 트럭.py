from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0])
    trucks = deque(truck_weights)
    sum_ = 0
    while q:
        if not trucks:
            answer += bridge_length
            q= []
        else:
            if len(q) >= bridge_length:
                sum_ -= q.popleft()
            if len(q) < bridge_length:
                # if trucks:
                    tmp = trucks.popleft()
                    if sum_+tmp <= weight:
                        q.append(tmp)
                        sum_ += tmp
                    else:
                        trucks.appendleft(tmp)
                        q.append(0)
                # else:
                #     q.append(0) 
            answer += 1
    
    return answer