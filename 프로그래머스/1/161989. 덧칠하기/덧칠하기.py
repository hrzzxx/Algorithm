def solution(n, m, section):
    answer = 0
    sec = set(section)
    
    # section만 순회하는 것이 핵심!
    for i in section: # 칠해야하는 구역 순회
        if i in sec: # 구역이 아직 칠해지지 않음
            cur = set(range(i,i+m)) # 현재 구역부터 롤러 길이까지의 구간
            # 현재 구간에서 칠해야하는 구역 번호 색칠 (칠해야 할 집합에서 삭제)
            sec -= cur
            answer += 1
            if not sec: break # 더이상 칠할게 없으면 순회 중단
    return answer