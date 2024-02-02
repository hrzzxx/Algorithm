import sys
input = sys.stdin.readline

s, e, q = input().rstrip().split()

d = dict()
set_ = set()
while True:
    try:
        time, name = input().rstrip().split()
        if time <= s:
            d[name] = time
        elif e <= time <= q:
            if name in d.keys():
                set_.add(name)
    except:
        break
print(len(set_))