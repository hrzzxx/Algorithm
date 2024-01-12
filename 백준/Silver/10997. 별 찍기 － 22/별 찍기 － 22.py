def sol(number):
    if number == 1: 
        print('*')
        return 
    nn = 1+(4*(number-1))
    tmp = (nn-3) //2
    a = 0
    li = []
    print('*'*nn)
    for j in range(nn//2+1):
        print('*', end=' ')
        if j%2==0:
            if a > 0:
                li.append(a)
                a += 2
            if li:
                for i in range(1,tmp+1):
                    print('*', end='') if i in li else print(end=' ')
                print(' ', end='')
                for i in range(tmp,0,-1):
                    print('*', end='') if i in li else print(end=' ')
            print()
        else:
            if a == 0: 
                print('*'*(nn-2))
                a = 1
                continue
            
            for i in range(tmp):
                print(end=' ') if i in li else print('*', end='')

            for i in range(tmp,0,-1):
                print(end=' ') if i in li else print('*', end='')
            print('*')
    for k in range(nn):
        if k%2==0: print('*',end='')
        else: print(' ', end='')
    print()
    for j in range(nn//2-1):
        print('*', end=' ')
        if j%2==0:
            if li:
                temp = ''
                for i in range(tmp,0,-1):
                    if i in li: temp += '*' 
                    else: temp += ' '
                li.pop()
                for i in range(1,tmp+1):
                    print('*', end='') if i in li else print(end=' ')
                print(' '+temp)
        else:
            if a == 0: 
                print('*'*(nn-2))
                a = 1
                continue
            for i in range(tmp):
                print(end=' ') if i in li[:-1] else print('*', end='')

            for i in range(tmp,0,-1):
                print(end=' ') if i in li else print('*', end='')
            print('*')
    print('*'*nn)
        

sol(int(input()))


