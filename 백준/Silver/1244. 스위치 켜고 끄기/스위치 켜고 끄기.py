import sys
input = sys.stdin.readline

s_n = int(input())
s = list(map(int, input().split()))

st_n = int(input())

for i in range(st_n):
    st_sex, k = map(int,input().split())
    if st_sex == 1:
        for i in range(k-1,len(s),k):
            if s[i]: s[i] = 0
            else: s[i] = 1
    else:
        range_ = min(k-1, len(s)-k)
        k -= 1
        for i in range(1,range_+1):
            if k-i <0: break
            if s[k-i] == s[k+i]:
                if s[k-i]: s[k-i], s[k+i] = 0,0
                else: s[k-i], s[k+i] = 1,1
            else:
                break
        if s[k]: s[k] = 0
        else: s[k] = 1
cnt = 1
for i in s:
    print(i, end=' ')
    if not cnt % 20: print()
    cnt += 1