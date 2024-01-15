import sys
input = sys.stdin.readline

def solution(s):
    st = []
    for i in s:
        if i == '(': st.append(1)
        elif i == '[': st.append(0)
        elif i == ')': 
            if st:
                if st[-1]: st.pop()
                else: return 'no'
            else: return 'no'
        elif i == ']': 
            if st:
                if not st[-1]: st.pop()
                else: return 'no'
            else: return 'no'
    if not st: return 'yes'
    else: return 'no'
while True:
    s = input().rstrip()
    if s == '.': break
    print(solution(s))