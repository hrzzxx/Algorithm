n = int(input())
tmp = sum([i+1 for i in range(n)])
tmp3 = sum([(i+1)**3 for i in range(n)])
print(tmp, tmp**2, tmp3, sep='\n')