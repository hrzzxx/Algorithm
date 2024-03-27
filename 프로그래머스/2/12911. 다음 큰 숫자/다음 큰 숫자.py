def solution(n):
    answer = 0
    cnt = str(bin(n)).count("1")
    
    while True:
        n+=1
        tmp = str(bin(n)).count("1")
        if tmp == cnt:
            return n