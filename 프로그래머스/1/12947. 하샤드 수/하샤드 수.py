def solution(x):
    n = 0
    for i in str(x):
        n += int(i)
    if not x%n: return True
    return False