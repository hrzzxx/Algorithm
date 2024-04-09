def solution(cards1, cards2, goal):
    answer = "Yes"
    cards1, cards2 = cards1[::-1], cards2[::-1]
    c1, c2 = cards1.pop(), cards2.pop()
    for i in goal:
        if i == c1:
            if cards1: c1 = cards1.pop()
        elif i == c2:
            if cards2: c2 = cards2.pop()
        else:
            return "No"
    return answer