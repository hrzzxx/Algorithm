def solution(s):
    s = [int(i) for i in s.split()]
    answer = f'{min(s)} {max(s)}'
    return answer