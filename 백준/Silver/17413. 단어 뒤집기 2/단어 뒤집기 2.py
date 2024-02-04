s = input()

st = []
idx = 0
while True:
    
    if idx >= len(s): break
    if s[idx] == '<':
        while s[idx] != '>':
            print(s[idx], end='')
            idx += 1
            if idx == len(s): break
        print(s[idx], end='')
        idx += 1
    elif s[idx] == ' ':
        print(' ', end='')
        idx += 1
    else:
        while s[idx] not in [' ', '<']:
            st.append(s[idx])
            idx += 1
            if idx == len(s): break
        print(''.join(st)[::-1], end='')
        st = []