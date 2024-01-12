import sys
input = sys.stdin.readline

def solution(s):
    s = s.split('+')
    nums = []
    for i in s:
        i = i.split('-')
        if len(i) == 1: nums.append(int(i[0]))
        else:
            if not i[0]:
                for x in i[1:]: nums.append(-int(x))
            else:
                nums.append(int(i[0]))
                for x in i[1:]: nums.append(-int(x))
    for i in range(len(nums)-1):
        if nums[i+1] > 0:
            if nums[i] < 0: 
                nums[i+1] = -(-nums[i]+ nums[i+1])
                nums[i] = 0
            else:
                nums[i+1] = nums[i]+ nums[i+1]
                nums[i] = 0
    return sum(nums)

print(solution(input().strip()))