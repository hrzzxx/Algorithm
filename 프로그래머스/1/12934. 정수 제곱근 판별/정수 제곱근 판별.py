import math
def solution(n):
    answer = 0
    if math.sqrt(n)%1 == 0:
        return (math.sqrt(n)+1)**2
    return -1