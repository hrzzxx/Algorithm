import sys
import itertools
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums == [0]: break
    k = nums[0]
    nums = nums[1:]
    for i in list(itertools.combinations(nums, 6)):
        print(*i)
    print()