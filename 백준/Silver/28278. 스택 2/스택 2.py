import sys
input = sys.stdin.readline

def solution(n):
    st = []
    for _ in range(n):
        ex = input().strip().split()
        if len(ex) == 1:
            ex = int(ex[0])
            if ex == 2:
                if st: print(st.pop())
                else: print(-1)
            elif ex == 3: print(len(st))
            elif ex == 4:
                if st: print(0)
                else: print(1)
            else:
                if st: print(st[-1])
                else: print(-1)
        else: st.append(int(ex[1]))
solution(int(input()))