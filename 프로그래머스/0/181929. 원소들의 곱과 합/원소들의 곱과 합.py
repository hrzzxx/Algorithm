def solution(num_list):
    answer = 0
    a = 1
    for i in num_list:
        a*= i
    b = sum(num_list)**2
    if a < b: return 1
    return answer