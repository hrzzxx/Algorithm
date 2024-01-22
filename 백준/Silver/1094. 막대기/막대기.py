import sys
input = sys.stdin.readline

x = int(input())
stick = [64]
while True:
    if sum(stick) > x:
        stick.sort()
        tmp = stick[0] // 2
        stick = stick[1:]
        if sum(stick) + tmp >= x:
            stick.append(tmp)
        else: 
            stick.append(tmp)
            stick.append(tmp)
    else: break
print(len(stick))