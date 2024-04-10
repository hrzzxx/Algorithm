def fn(x):
    cnt=0
    for i in range(1,x+1):
        if i*i >= x: 
            if i*i == x: cnt += 1
            break
        elif not x%i: cnt += 2
    return cnt
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        p = fn(i)
        if p > limit:
            answer += power
        else:
            answer += p
    return answer