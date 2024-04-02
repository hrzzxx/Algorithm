def solution(n, lost, reserve):
    answer = 0
    reserve = set(reserve)
    lost_copy = set(lost)
    tmp = reserve & lost_copy
    lost_copy -= tmp 
    reserve -= tmp
    for i in list(lost_copy):
        if i-1 in reserve:
            lost_copy -= {i}
            reserve -= {i-1}
        elif i+1 in reserve:
            lost_copy -= {i}
            reserve -= {i+1}
    return n - len(lost_copy)