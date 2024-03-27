def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        tmp = discount[i:i+10]
        check = 1
        for i,w in enumerate(want):
            if not tmp.count(w) == number[i]:
                check = 0
                break
        if check: answer += 1
    return answer