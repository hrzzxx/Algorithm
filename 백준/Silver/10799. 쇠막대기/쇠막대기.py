import sys
input = sys.stdin.readline

input_ = input().rstrip()

st = []
res = 0
for i,l in enumerate(input_):
    if l== '(':
        st.append(i)
    else:
        s = st.pop()
        if i-s == 1:
            res += len(st)
        else:
            res += 1
print(res)