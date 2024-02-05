eng = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
engd = {i:0 for i in eng}

while True:
    try:
        s = list(''.join(input().split()))
        for i in s: engd[i] += 1
    except EOFError: break

engd = sorted(engd.items(), key=lambda x:(-x[1], x[0]))
tmp = engd[0][1]
for a, n in engd:
    if n < tmp: break
    print(a,end='')