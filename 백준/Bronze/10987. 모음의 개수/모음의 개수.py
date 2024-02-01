s = input().rstrip()
v = list('a e i o u')
res = 0
for i in s:
    if i in v: res += 1
print(res)