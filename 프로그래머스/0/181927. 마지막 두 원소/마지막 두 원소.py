def solution(num_list):
    answer = []
    a, b = num_list[-1], num_list[-2]
    if a > b:
        return num_list + [a-b]
    else:
        return num_list+[a*2]
    return answer