def solution(numbers):
    numbers = set(numbers)
    tmp = {0,1,2,3,4,5,6,7,8,9}
    tmp = tmp - numbers
    return sum(tmp)