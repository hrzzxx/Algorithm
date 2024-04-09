def convert(x, n):
    x = bin(x)[2:]
    if len(x) != n:
        x = '0'*(n-len(x))+x
    return x
def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a,b = convert(a,n), convert(b,n)
        res = ''
        for i,j in zip(a,b):
            if int(i) or int(j): res += '#'
            else: res += ' '
        answer.append(res)
    return answer