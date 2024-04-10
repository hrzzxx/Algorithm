n = list(map(int, list(input())))
if len(n) ==1: n += [0]
ans = n
res = 0
while True:
    n = [n[-1],sum(n)%10]
    res += 1
    if n == ans: break
print(res)