import sys
input = sys.stdin.readline

while True:
    na, nb = map(int, input().split())
    if (na, nb) == (0,0): break
    a = {int(input()) for _ in range(na)}
    b = {int(input()) for _ in range(nb)}

    print(len(a&b))
