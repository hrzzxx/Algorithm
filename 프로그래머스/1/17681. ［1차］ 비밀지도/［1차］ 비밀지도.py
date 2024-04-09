def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        res = bin(a|b)[2:]
        if len(res) != n:
            res = '0'*(n-len(res))+res
        res = ''.join(['#' if int(i) else ' ' for i in res])
        answer.append(res)
        print(res)
    return answer