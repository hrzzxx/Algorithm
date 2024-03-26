def convert(s, n, i):
    while n in s:
        s = s.replace(n, str(i))
    return s
def solution(s):
    answer = 0
    li = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i, n in enumerate(li):
        s = convert(s,n,i)
    return int(s)