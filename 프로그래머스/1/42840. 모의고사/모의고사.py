def solution(answers):
    answer = []
    l = len(answers)
    a = [1, 2, 3, 4, 5] *10000
    b = [2, 1, 2, 3, 2, 4, 2, 5] *10000
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *10000
    
    li = [0,0,0]
    for _a, _b, _c, _ans in zip(a[:l], b[:l], c[:l], answers):
        if _ans == _a: li[0]+= 1
        if _ans == _b: li[1]+= 1
        if _ans == _c: li[2]+= 1
    cnt = li.count(max(li))
    if cnt == 3:
        return [1,2,3]
    elif cnt == 2:
        res = []
        for i,x in enumerate(li):
            if x == max(li): res.append(i+1)
        return res
    else:
        return [li.index(max(li))+1]