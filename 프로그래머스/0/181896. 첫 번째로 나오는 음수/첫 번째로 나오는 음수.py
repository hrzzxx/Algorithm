def solution(num_list):
    answer = -1
    for i,x in enumerate(num_list):
        if x<0:return i
    return answer