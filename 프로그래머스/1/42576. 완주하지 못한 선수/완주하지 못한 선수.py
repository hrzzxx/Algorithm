def solution(participant, completion):
    p = dict()
    for i in participant:
        if i in p: p[i] += 1
        else: p[i] = 1
    for i in completion:
        p[i] -= 1
        if not p[i]: del p[i]
    return list(p.keys())[0]