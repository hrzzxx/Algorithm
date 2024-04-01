def solution(s):
    s = s.lower()
    s = list(s)
    if s.count('p') == s.count('y'): return True

    return False