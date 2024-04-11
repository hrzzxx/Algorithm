import itertools
import math
def solution(nums):
    comb = list(sum(i) for i in list(itertools.combinations(nums,3)))
    max_ = int(math.sqrt(max(comb)))
    li = list(range(max(comb)+1))
    for i in range(2,max_+1):
        if li[i]:
            for j in range(i*2,len(li),i):
                if not j%i: li[j] = 0
    li = set(li[2:]) - {0}
    answer = 0
    for i in comb:
        if i in li: answer += 1
    return answer