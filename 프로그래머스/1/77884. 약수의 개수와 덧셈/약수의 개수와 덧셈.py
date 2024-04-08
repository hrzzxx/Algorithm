def tmp(x):
    if x == 1: return False
    cnt = 2
    for i in range(2,x):
        if not x%i: cnt += 1
    if cnt%2: return False
    return True
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if tmp(i): answer += i
        else: answer -= i
    return answer