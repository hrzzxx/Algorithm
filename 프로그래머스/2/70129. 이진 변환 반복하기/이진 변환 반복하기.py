def convert(s):
    cnt = s.count("1")
    b = str(bin(cnt))[2:]
    return b, s.count("0")
def solution(s):
    answer = [0,0]
    while s != "1":
        s, z = convert(s)
        answer[0] += 1
        answer[1] += z
    return answer