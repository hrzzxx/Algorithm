def _solution(arr, i, j, k):
    arr = arr[i-1:j]
    arr.sort()
    return arr[k-1]
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        answer.append(_solution(array, i, j, k))
    return answer