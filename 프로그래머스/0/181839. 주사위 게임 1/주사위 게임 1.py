def tmp(x):
    if not x%2: return 1 # 짝수
    else: return 0
def solution(a, b):
    answer = 0
    _a, _b = tmp(a), tmp(b)
    if not _a and not _b:
        return a**2 + b**2
    elif not _a or not _b:
        return 2*(a+b)
    else:
        return abs(a-b)
    return answer