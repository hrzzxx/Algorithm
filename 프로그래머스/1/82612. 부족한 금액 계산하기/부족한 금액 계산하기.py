def solution(price, money, count):
    answer = sum([price*(i+1) for i in range(count)]) - money
    if answer <= 0: return 0
    return answer