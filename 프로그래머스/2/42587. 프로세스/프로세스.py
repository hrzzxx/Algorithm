from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque(zip(range(len(priorities)),priorities))
    tmp = priorities
    tmp.sort()
    while q:
        i, rank = q.popleft()
        if rank == max(tmp):
            if i == location:
                print(rank)
                return answer + 1
            answer += 1
            tmp.pop()
        else:
            q.append((i, rank))
    return answer