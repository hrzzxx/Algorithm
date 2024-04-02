import itertools
def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = list(set(nums))
    if n > len(nums):
        return len(nums)
    else:
        return n
    # return len(nums)