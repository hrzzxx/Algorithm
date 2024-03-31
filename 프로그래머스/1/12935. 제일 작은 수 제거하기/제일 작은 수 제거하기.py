def solution(arr):
    del arr[arr.index(min(arr))]
    if not arr: arr = [-1] 
    return arr