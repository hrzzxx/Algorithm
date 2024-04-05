from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    _max = -1
    prices = deque(zip(range(len(prices)),prices))
    st = []
    while prices:
        i, p = prices.popleft()
        if p < _max: # 가격이 떨어질 때
            _i, _p = st.pop()
            try:
                while _p > p:
                    answer[_i] = i - _i
                    _i, _p = st.pop()
                st.append((_i,_p))
            except:
                pass
        _max = p
        st.append((i,p))
    for idx, _ in st:
        answer[idx] = i-idx
            
    return answer