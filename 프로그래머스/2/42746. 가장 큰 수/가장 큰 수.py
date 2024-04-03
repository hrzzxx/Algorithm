from functools import cmp_to_key
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=cmp_to_key(lambda x, y: 1 if x+y > y+x else -1))
    return str(int(''.join(numbers)))