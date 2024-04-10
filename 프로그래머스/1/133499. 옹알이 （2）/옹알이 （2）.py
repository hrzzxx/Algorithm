def solution(babbling):
    answer = 0
    li = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        if word in li:
            answer += 1
        else:
            tmp = [1,2,3,4]
            for i,w in enumerate(li):
                if w in word:
                    word = word.replace(w,str(tmp[i]))
            if word.isdigit():
                cur = ''
                for i in word:
                    if i == cur: 
                        answer -= 1
                        break
                    cur = i
                answer += 1
    return answer