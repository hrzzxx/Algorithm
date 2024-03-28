def solution(brown, yellow):
    for i in range(brown//2-1,2,-1):
        tmp = brown-i*2
        a, b = i*2+tmp, tmp//2*(i-2)
        if a == brown and b == yellow:
            return [i,tmp//2+2]