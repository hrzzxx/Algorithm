import sys
input = sys.stdin.readline

for i in range(int(input())):
    li = input().rstrip().split()
    d = dict()
    while True:
        s = input().rstrip()
        if s == 'what does the fox say?': break
        sound = s.split()[-1]
        d[sound] = 1
    for i in li:
        if i not in d: print(i, end=' ')
    print()