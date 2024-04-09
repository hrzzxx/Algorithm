def solution(k, score):
    answer = []
    rank = []
    for i in score:
        if len(rank) < k:
            rank.append(i)
        else:
            _min = min(rank)
            if _min < i:
                rank.pop(rank.index(_min))
                rank.append(i)
        answer.append(min(rank))
    return answer