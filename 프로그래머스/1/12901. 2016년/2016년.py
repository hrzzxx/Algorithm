def solution(a, b):
    days = "THU,FRI,SAT,SUN,MON,TUE,WED".split(',')
    m = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = days[(sum(m[:a-1])+b)%7]
    return answer