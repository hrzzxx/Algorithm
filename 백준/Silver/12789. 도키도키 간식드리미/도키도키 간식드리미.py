import sys
input = sys.stdin.readline

def solution(n):
    li = list(map(int, input().split()))
    st = []
    cur = 1
    for i in range(n):
        st.append(li[i])
        if cur == li[i]:
            while st[-1] == cur:
                st.pop()
                cur += 1
                if not st: break
    if st: return 'Sad'
    else: return 'Nice'
print(solution(int(input())))