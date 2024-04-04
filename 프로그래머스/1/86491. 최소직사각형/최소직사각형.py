def solution(sizes):
    w, h = -1, -1
    for s in sizes:
        a, b = s
        if a > b:
            a, b = b, a
        if w < a: w = a
        if h < b: h = b
    return w*h