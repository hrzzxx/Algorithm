import math
def solution(n):
    answer = 0
    li = list(range(n+1))
    m = int(math.sqrt(n))
    for i in range(2,m+1):
        if li[i]:
            for j in range(i*2,n+1,i):
                if not li[j]%i:li[j] = 0
    answer = len(set(li[2:]) - {0})
    return answer