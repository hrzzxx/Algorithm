def solution(n, words):
    cur = ''
    li = [words[0]]
    for i, w in enumerate(words):
        if not cur: cur = w[-1]
        else:
            if cur == w[0] and w not in li: 
                cur = w[-1]
                li.append(w)
            else: 
                return [i%n+1, i//n+1]
    return [0,0]