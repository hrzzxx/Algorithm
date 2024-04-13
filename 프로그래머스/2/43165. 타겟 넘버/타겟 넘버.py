from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([(numbers[0],0),(-numbers[0],0)])
    while q:
        tmp, idx = q.popleft()
        try:
            q.append((tmp+numbers[idx+1],idx+1))
            q.append((tmp-numbers[idx+1],idx+1))
        except:
            if tmp == target: answer += 1
    return answer