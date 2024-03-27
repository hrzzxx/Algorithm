from collections import deque
def solution(s):
    cur = ''
    s = deque(list(s))
    st = []
    while s:
        if not st: st.append(s.popleft())
        if not s: return 0
        a, b = st.pop(), s.popleft()
        if a != b:
            st.append(a)
            st.append(b)
        
    if st: return 0
    return 1