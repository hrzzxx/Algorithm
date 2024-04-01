def cal(num):
    if not num%2: return num//2
    else: return num*3 + 1
def solution(num):
    answer = 0
    if num == 1: return 0

    while True:
        num = cal(num)
        answer += 1
        if num == 1: return answer
        if answer > 500: return -1