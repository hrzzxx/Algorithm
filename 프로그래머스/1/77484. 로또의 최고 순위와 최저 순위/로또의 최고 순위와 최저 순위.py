def solution(lottos, win_nums):
    f = lottos.count(0) # 알지 못하는 로또 번호의 개수
    x, y = set(lottos) - {0}, set(win_nums)
    s = len(x&y)
    tmp = 7
    if not f and not s: tmp = 6
    answer = [tmp-(f+s), tmp-s]
    if not s: answer[1] = 6
    return answer